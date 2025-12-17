from simulators.event import Event, EventType
from stations.station import Station

# Iniettatore di Clienti.

class ClientGenerator(Station):
    distribution = None

    def __init__(self, next_station, observer, simulator, distribution):
        super().__init__("gen", observer, simulator)
        self.next_station = next_station
        self.distribution = distribution
        time = distribution.next_sample()
        evt = Event(time, self, EventType.DEPARTURE)
        simulator.schedule_event(evt)

    def client_departure(self, event):
        evt = Event(0,  self.next_station, EventType.ARRIVAL)
        self.simulator.schedule_event(evt)
        time = self.distribution.next_sample()
        evt = Event(time,  self, EventType.DEPARTURE)
        self.simulator.schedule_event(evt)

    def reset(self):
        time = self.distribution.next_sample()
        evt = Event(time, self, EventType.DEPARTURE)
        self.simulator.schedule_event(evt)