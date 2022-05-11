from event import Event


class Observer:
    client_arrived:int =0
    client_departed:int =0
    working_time:int=0
    area=0
    last_area_mod=0
    last_area_value=0
    temp_time=0
    def client_arrival(self, time):
        self.client_arrived +=1
        self.area += self.last_area_value * (time - self.last_area_mod)
        self.last_area_value +=1
        self.last_area_mod = time

    def client_departure(self, time):
        self.client_departed += 1

        self.area += self.last_area_value*(time-self.last_area_mod)
        self.last_area_value -= 1
        self.last_area_mod = time

    def client_service_start(self, time):
        self.temp_time=time

    def client_service_stop(self,time):
        self.working_time += self.temp_time
        self.temp_time=0

    def get_utilizzazione(self,time):
        return self.working_time/time

    def get_throughput(self,time):
        return self.client_departed/(time/1000)

    def get_mean_client_queue_or_service(self, time):
        self.area += self.last_area_value * (time - self.last_area_mod)
        self.last_area_mod=time
        return self.area/time

    def get_waiting_time(self,time):
        arrival_rate=self.client_arrived/(time/1000)
        return self.get_mean_client_queue_or_service(time)/arrival_rate


    def ouput(self,time):
        print("Simulated time: \n"+ str(time))
        print("Arrived client:  "+str(self.client_arrived)+"   Departed client:    "+str(self.client_departed)+"\n")
        print("client arrival rate:"+str(self.client_arrived/(time/1000)))
        print("throughput:" + str(self.get_throughput(time)))
        print("utilizzazione servente:" + str(self.get_utilizzazione(time)))
        print("mean number client in line or in service:" + str(self.get_mean_client_queue_or_service(time)))
        print("Waiting time in line or in service:" + str(self.get_waiting_time(time)))