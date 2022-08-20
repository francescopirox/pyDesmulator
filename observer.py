from event import Event


# Classe Base Observer

class Observer:
    client_arrived: int = 0
    client_departed: int = 0
    working_time: int = 0
    area: float = 0
    last_area_mod: int = 0
    last_area_value: int = 0
    temp_work_time: int = 0
    waiting_time: int = 0
    arrival_time_list = []

    def client_arrival(self, time_stamp):
        self.client_arrived += 1
        self.area += self.last_area_value * (time_stamp - self.last_area_mod)
        self.last_area_value += 1
        self.last_area_mod = time_stamp
        self.arrival_time_list.append(time_stamp)

    def client_departure(self, time_stamp):
        if self.client_arrived - self.client_departed > 0:
            self.client_departed += 1

            self.area += self.last_area_value * (time_stamp - self.last_area_mod)
            self.last_area_value -= 1
            self.last_area_mod = time_stamp

            self.waiting_time += time_stamp - self.arrival_time_list.pop(0)

    def client_service_start(self, work_time:int,time_stamp:int=-1):
        if self.client_arrived - self.client_departed > 0:
            self.temp_work_time = work_time

    def client_service_stop(self, time_stamp:int):
        if self.client_arrived - self.client_departed > 0:
            self.working_time += self.temp_work_time
            self.temp_work_time = 0

    def get_utilizzazione(self, time):
        return self.working_time / time

    def get_throughput(self, time):
        return self.client_departed / (time / 1000)

    def get_mean_client_queue_or_service(self, time):
        self.area += self.last_area_value * (time - self.last_area_mod)
        self.last_area_mod = time
        return self.area / time

    def get_waiting_time(self):
        return (self.waiting_time / 1000) / self.client_departed

    def get_waiting_time_little(self, time):
        arrival_rate = self.client_arrived / (time / 1000)
        return self.get_mean_client_queue_or_service(time) / arrival_rate

    ##TEST
    def output(self, time):
        print("Simulated time: \n" + str(time))
        print("Arrived client:  " + str(self.client_arrived) + "   Departed client:    " + str(
            self.client_departed) + "\n")
        print("client arrival rate:" + str(self.client_arrived / (time / 1000)))
        print("throughput:" + str(self.get_throughput(time)))
        print("utilizzazione servente:" + str(self.get_utilizzazione(time)))
        print("mean number client in line or in service:" + str(self.get_mean_client_queue_or_service(time)))

        print("Waiting time in line or in service:" + str(self.get_waiting_time()))
        print("Waiting time in line or in service little:" + str(self.get_waiting_time_little(time)))
