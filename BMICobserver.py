import math

from observer import Observer


class ObserverTime:
    time_stamp: int
    observer: Observer

    def __init__(self, time_stamp, observer) -> None:
        self.time_stamp = time_stamp
        self.observer = observer

    def __cmp__(self, other):
        if self.time_stamp > other.time_stamp:
            return 1
        elif self.time_stamp < other.time_stamp:
            return -1
        return 0


class Ic:
    mean_value: float
    quantile: float

    def __init__(self, mean_value, quantile) -> None:
        self.quantile = quantile
        self.mean_value = mean_value


class BMICObserver(Observer):
    dump: int
    transitorio: bool = True
    time_start_data: int = -1
    batch_number:int
    batch_size: int
    oss:int=0
    last:bool =False
    finish:bool = False

    observers: ObserverTime = []

    def __init__(self, batch_size: int, batch_number: int) -> None:
        super().__init__()
        self.dump = 0
        self.transitorio = False
        self.batch_size = batch_size
        self.batch_number = batch_number

    def __init__(self, dump: int, batch_size: int, batch_number: int) -> None:
        super().__init__()
        self.dump = dump
        self.batch_size = batch_size
        self.batch_number = batch_number

    def client_arrival(self, time: int):
        super().client_arrival(time)
        if self.client_arrived == self.dump:
            self.transitorio = False
            self.observers.append(ObserverTime(time, Observer()))
        if not self.transitorio:
            self.oss+=1
            self.observers[-1].observer.client_arrival(time - self.observers[-1].time_stamp)
            if(self.oss >= self.batch_number and len(self.observers)<self.batch_number):
                self.oss=0
                self.last=True
                self.observers.append(ObserverTime(time, Observer()))
                self.observers[-1].observer.client_arrival(time - self.observers[-1].time_stamp)

    def client_departure(self, time_stamp):
        super().client_departure(time_stamp)
        if not self.transitorio and not self.finish:
            if time_stamp is not self.observers[-1].time_stamp:
                self.observers[-1].observer.client_departure(time_stamp - self.observers[-1].time_stamp)

    def client_service_start(self, work_time):
        super().client_service_start(work_time)
        if not self.transitorio and not self.finish:
            if work_time is not self.observers[-1].time_stamp:
                self.observers[-1].observer.client_service_start(work_time)
            if self.last :
                self.finish=True
    def client_service_stop(self, time):
        super().client_service_stop(time)
        if not self.transitorio and not self.finish:
            if time is not self.observers[-1].time_stamp:
                    self.observers[-1].observer.client_service_stop(time)

    def get_waiting_time_ic(self, stop_time):
        values = []
        times=[]
        for observertype in self.observers:
            times.append(observertype.time_stamp)
        times.append(stop_time)
        times.sort()
        for observertype in self.observers:
            index=0
            for i in range(0, len(times)):
                if(times[i]==observertype.time_stamp):
                    index=i+1
                    break
            values.append(observertype.observer.get_waiting_time())

        return self.confidence_interval()

    def confidence_interval(self, values):
        if self.state():
            mean_value: float = 0
            n = len(values)
            std_dev: float = 0
            n: int = 0
            for value in values:
                mean_value += value
            mean_value = mean_value / n
            for value in values:
                std_dev += (value - mean_value) ^ 2
            std_dev /= (n - 1)
            std_dev = math.sqrt(std_dev)
            return Ic(mean_value, std_dev / math.sqrt(n))

    def state(self):
        return self.client_arrived > self.dump + (self.batch_size * self.batch_number)
