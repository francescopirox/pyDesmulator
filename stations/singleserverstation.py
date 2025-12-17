from distributions import Distribution
from simulators import Simulator
from simulators.event import Event, EventType
from stations.infinityStation import InfinityStation


# Stazione a Servente Singolo, sfrutta classe base Server

class SingleServerStation(InfinityStation):

    def __init__(self, observer, simulator: Simulator, distribution: Distribution):
        self.queue: int = 0
        self.server_free: bool = True
        super().__init__(observer, simulator, distribution)

    def client_arrival(self, event):
        if self.observer is not None:
            self.observer.client_arrival(event.time_stamp)
        if self.server_free:
            evt = Event(0, self, EventType.START_PROCESS)
            self.simulator.schedule_event(evt)
            self.server_free = False
        else:
            self.queue += 1

    def client_departure(self, event):
        super().client_departure(event)
        if self.queue > 0:
            self.queue -= 1
            evt = Event(0, self, EventType.START_PROCESS)
            self.simulator.schedule_event(evt)
        else:
            self.server_free = True

    def reset(self):
        self.queue=0
        self.server_free=True

    def print_state(self):
        super().print_state()
        print("Len queue: " + str(self.queue))
        print("Serv status:" + str(self.server_free))
