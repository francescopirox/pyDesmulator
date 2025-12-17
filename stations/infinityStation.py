from distributions.distribution import Distribution
from simulators.event import EventType, Event
from simulators.simulator import Simulator
from .station import Station

# Stazione con infiniti serventi, code illimitate

class InfinityStation(Station):
    distribution: Distribution = None

    def __init__(self, observer, simulator: Simulator, distribution: Distribution):
        super().__init__("", observer, simulator)
        self.distribution = distribution

    def service_client_start(self, event):
        time=self.distribution.next_sample()
        evt = Event(time, self, EventType.END_PROCESS)
        self.simulator.schedule_event(evt)
        self.observer.client_service_start(time,event.time_stamp)

    def reset(self):
        self.distribution.change_seed()
