import math

from observer import Observer
from observer_transitorio import Observer_transitorio


class BMICObserver(Observer):
    observer_time:int=0
    sim_time:int=0
    batch_number:int=0
    transitorio:int=0
    osservatori=[]

    def __init__(self, transitorio:int , sim_time , batch_number: int) -> None:
        super().__init__()
        self.sim_time=sim_time
        self.batch_number=batch_number
        self.transitorio=transitorio
        self.observer_time=(sim_time-transitorio)//batch_number
        for i in range(batch_number):
            self.osservatori.append(Observer_transitorio())

    def client_arrival(self, time_stamp, transitorio=False):
        index = time_stamp - self.transitorio // self.batch_number
        if(index < 0):
            index=0

        self.osservatori[index].client_arrival(time_stamp, time_stamp < self.transitorio)

    def client_departure(self, time_stamp, transitorio=False):
        index = time_stamp - self.transitorio // self.batch_number
        if (index < 0):
            index = 0

    def client_service_start(self, work_time: int, time_stamp: int = -1, transitorio=False):
        super().client_service_start(work_time, time_stamp, transitorio)

    def client_service_stop(self, time_stamp: int, transitorio=False):
        super().client_service_stop(time_stamp, transitorio)



