# Implementa il metodo delle repliche indipendenti
import math

from IC import Ic
from observer import Observer


def confidence_interval(values):
    mean_value: float = 0
    n = len(values)
    std_dev: float = 0
    for value in values:
        mean_value += value
    mean_value = mean_value / n
    for value in values:
        std_dev += (value - mean_value) ** 2
    std_dev /= (n - 1)
    std_dev = math.sqrt(std_dev)
    return Ic(mean_value, std_dev / math.sqrt(n))


class Icobserver(Observer):
    classi: int = 0
    transitorio:int=0
    sim_time = 0
    osservatori = []
    index = 0

    def __init__(self, classi, tempo, transitorio) -> None:
        super().__init__()
        self.classi = classi
        self.sim_time = tempo
        self.transitorio=transitorio
        for i in range(0, classi):
            self.osservatori.append(Observer())

    def cambia_osservatore(self):
        self.index += 1;

    def client_arrival(self, time_stamp):
        self.osservatori[self.index].client_arrival(time_stamp,time_stamp>self.transitorio)

    def client_departure(self, time_stamp):
        self.osservatori[self.index].client_departure(time_stamp,time_stamp>self.transitorio)

    def client_service_start(self, work_time,time_stamp):
        self.osservatori[self.index].client_service_start(work_time,time_stamp>self.transitorio)

    def client_service_stop(self, time_stamp):
        self.osservatori[self.index].client_service_stop(time_stamp,time_stamp>self.transitorio)

    def get_waiting_time_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_waiting_time())

        return confidence_interval(values)

    def get_throughput_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_throughput(self.sim_time))

        return confidence_interval(values)

    def get_utilizzazione_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_throughput(self.sim_time))

        return confidence_interval(values)

    def get_mean_client_queue_or_service_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_mean_client_queue_or_service(self.sim_time))

        return confidence_interval(values)

    ##TEST
    def output(self, time):
        print("Simulated time: \n" + str(time))
        print("Waiting time in line or in service IC 95: " + str(self.get_waiting_time_ic()))
        print("Throughput IC 95: " + str(self.get_throughput_ic()))
        print("Utilizzazione IC 95: " + str(self.get_utilizzazione_ic()))
        print("Queue len IC 95: " + str(self.get_mean_client_queue_or_service_ic()))

