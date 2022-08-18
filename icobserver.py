# Implementa il metodo delle repliche indipendenti
import math

from IC import Ic
from observer import Observer


class Icobserver(Observer):
    classi: int = 0
    sim_time = 0
    osservatori = []
    index = 0

    def __init__(self, classi, tempo) -> None:
        super().__init__()
        self.classi = classi
        self.sim_time = tempo
        for i in range(0, classi):
            self.osservatori.append(Observer())

    def cambia_osservatore(self):
        self.index += 1;

    def client_arrival(self, time_stamp):
        self.osservatori[self.index].client_arrival(time_stamp)

    def client_departure(self, time_stamp):
        self.osservatori[self.index].client_departure(time_stamp)

    def client_service_start(self, work_time):
        self.osservatori[self.index].client_service_start(work_time)

    def client_service_stop(self, time):
        self.osservatori[self.index].client_service_stop(time)

    def get_waiting_time_ic(self):
        values = []
        for observer in self.osservatori:
            values.append(observer.get_waiting_time())

        return self.confidence_interval(values)

    def confidence_interval(self, values):
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

    ##TEST
    def output(self, time):
        print("Simulated time: \n" + str(time))
        print("Waiting time in line or in service IC 95:" + str(self.get_waiting_time_ic()))
