

# Classe Base Observer
from observer import Observer


class Observer_transitorio(Observer):
    time_transitorio=0
    uscito=False
    client_arrived_after=0
    client_departed_after = 0
    area = 0
    last_area_value = 0



    def client_arrival(self, time_stamp, transitorio=False):
        if not transitorio:
            if not self.uscito:

                self.time_transitorio=time_stamp
                self.uscito=True
            self.client_arrived_after +=1
            self.area += self.last_area_value * (time_stamp - self.last_area_mod)
        self.client_arrived+=1
        self.last_area_value += 1
        self.last_area_mod = time_stamp
        self.arrival_time_list.append(time_stamp)

    def client_departure(self, time_stamp,transitorio=False):
        if self.client_arrived - self.client_departed > 0:
            if not transitorio:
                if not self.uscito:

                    self.time_transitorio = time_stamp
                    self.uscito = True
                self.client_departed_after += 1
                self.area += self.last_area_value * (time_stamp - self.last_area_mod)
            self.client_departed += 1
            self.last_area_value -= 1
            self.last_area_mod = time_stamp
            if not transitorio:
                self.waiting_time += time_stamp - self.arrival_time_list.pop(0)
            else:
                self.arrival_time_list.pop(0)

    def client_service_start(self, work_time:int,time_stamp:int=-1, transitorio=False):
        if self.client_arrived - self.client_departed > 0 and not transitorio:
            self.temp_work_time = work_time
            if not self.uscito:

                self.time_transitorio = time_stamp
                self.uscito = True

    def client_service_stop(self, time_stamp:int,transitorio=False):
        if self.client_arrived - self.client_departed and not transitorio > 0:
            self.working_time += self.temp_work_time
            self.temp_work_time = 0
            if not self.uscito:
                self.time_transitorio = time_stamp
                self.uscito = True

    def get_utilizzazione(self, time):
        return self.working_time / (time-self.time_transitorio)

    def get_throughput(self, time):
        return self.client_departed_after / ((time-self.time_transitorio)/ 1000)

    def get_mean_client_queue_or_service(self, time):
        self.area += self.last_area_value * (time - self.last_area_mod)
        self.last_area_mod = time
        return self.area / (time-self.time_transitorio)

    def get_waiting_time(self):
        return (self.waiting_time/1000) / self.client_departed_after

    def get_waiting_time_little(self, time):
        arrival_rate = self.client_arrived / ((time-self.time_transitorio) / 1000)
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
