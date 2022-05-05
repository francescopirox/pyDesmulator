import simulator
from event import Event

class Station:
    next_station = None
    observer = None
    simulator = None

    def __init__(self,next_station,observer,simulator):
        self.next_station=next_station
        self.observer=observer
        self.simulator = simulator
        self.simulator.station_bind(self)

    def receive_event(self, event):
        print(str(event)+ "ciaooo")

    def start(self):
        print("stazione partita")
        evt = Event(1000, self, self.next_station)
        self.simulator.schedule_event(evt)

    def service_client_start(self,event):
        evt= Event(event.time_stamp+1,self,self)
        self.simulator.schedule_event(evt)

    def service_client_stop(self,event):
        evt = Event(event.time_stamp + 1000, self, self.next_station)
        self.simulator.schedule_event(evt)