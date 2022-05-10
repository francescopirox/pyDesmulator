from distribution import Distribution
from event import EventType, Event
from simulator import Simulator
from station import Station


class InfinityStation(Station):
    distribution: Distribution = None

    def __init__(self, observer, simulator: Simulator, distribution: Distribution):
        super().__init__("", observer, simulator)
        self.distribution = distribution

    def service_client_start(self, event):
        super().service_client_start(event)
        evt = Event(self.distribution.next_sample(), self, EventType.END_PROCESS)
        self.simulator.schedule_event(evt)
