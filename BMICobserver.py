import math

from icobserver import confidence_interval
from observer import Observer
from observer_transitorio import Observer_transitorio


class BMICObserver(Observer):
    observer_time:int=0
    sim_time:int=0
    batch_number:int=0
    transitorio:int=0
    osservatori=[]

    def __init__(self, transitorio:int , sim_time:int , batch_number: int) -> None:
        super().__init__()
        self.sim_time=sim_time
        self.batch_number=batch_number
        self.transitorio=transitorio
        self.observer_time=(sim_time-transitorio)//batch_number
        for i in range(batch_number):
            self.osservatori.append(Observer_transitorio())

    def client_arrival(self, time_stamp, transitorio=False):
        index = (time_stamp - self.transitorio) //((self.sim_time-self.transitorio)// self.batch_number)
        if(index < 0):
            index=1

        self.osservatori[index-1].client_arrival(time_stamp, time_stamp < self.transitorio)

    def client_departure(self, time_stamp, transitorio=False):
        index = (time_stamp - self.transitorio) //((self.sim_time-self.transitorio)// self.batch_number)
        if (index < 0):
            index = 0

        self.osservatori[index-1].client_departure(time_stamp, time_stamp < self.transitorio)

    def client_service_start(self, work_time: int, time_stamp: int = -1, transitorio=False):
        index = (time_stamp - self.transitorio) //((self.sim_time-self.transitorio)// self.batch_number)
        if (index < 0):
            index = 0

        self.osservatori[index-1].client_service_start(work_time, time_stamp < self.transitorio)

    def client_service_stop(self, time_stamp: int, transitorio=False):

        index = (time_stamp - self.transitorio) //((self.sim_time-self.transitorio)// self.batch_number)
        if (index < 0):
            index = 0
            self.osservatori[index-1].client_service_stop(time_stamp, time_stamp < self.transitorio)

    def get_waiting_time_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_waiting_time())
        print(values)
        return confidence_interval(values)

    def output(self, time):
        print("Simulated time: \n" + str(time))
        print("Waiting time in line or in service IC 95: " + str(self.get_waiting_time_ic()))




