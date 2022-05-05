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
        if len(self.event_list)==0:
            raise Exception("Simulation DeadLock")
        evt=self.event_list.pop()
        if evt.arrival_station is not None:
            evt.arrival_station.receive_event(evt)
        self.time_advance()

    def time_advance(self):
        print(self.time)
        if len(self.event_list) == 0:
            raise Exception("Simulation DeadLock")
        next_evt=self.event_list[0]
        if next_evt.time_stamp > self.time:
            self.time=next_evt.time_stamp

    def start_simulation(self):
        if len(self.station_list)==0:
            raise Exception("no station binded to the simulator")
        for s in self.station_list:
            s.start()
        self.time_advance()
        self.process()

    def station_bind(self, station):
        self.station_list.append(station)