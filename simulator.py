import event


class Simulator:
    time=0
    end_time=0
    event_list=[]
    station_list=[]

    def __init__(self, end_time) -> None:
        super().__init__()
        self.end_time=end_time

    def schedule_event(self,event):
        self.event_list.append(event)
        self.event_list.sort()

    def process(self):
        while self.time < self.end_time:
            if len(self.event_list)==0:
                raise Exception("Simulation DeadLock")
            evt=self.event_list.pop()
            if evt is None:
                raise Exception("evt is none")

            if evt.type is not event.EventType.NULL:
                pass
            if evt.type is event.EventType.DEPARTURE:
                evt.departure_station.client_departure(evt)

            if evt.type is event.EventType.ARRIVAL:
                evt.arrival_station.client_arrival(evt)

            if evt.type is event.EventType.START_PROCESS:
                evt.departure_station.service_client_start(evt)

            if evt.type is event.EventType.END_PROCESS:
                evt.departure_station.service_client_stop(evt)

            self.time_advance()

    def time_advance(self):
        print(self.time)
        if len(self.event_list) == 0:
            raise Exception("Simulation DeadLock")
        next_evt=self.event_list[0]
        if next_evt.time_stamp > self.time:
            self.time=next_evt.time_stamp

    def start_simulation(self):
        self.time_advance()
        self.process()

    def station_bind(self, station):
        self.station_list.append(station)