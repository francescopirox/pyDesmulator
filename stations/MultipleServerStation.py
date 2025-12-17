from . import InfinityStation
from distributions import Distribution
from simulators import *


#Multiple server station omogeneus service time.
class MultipleServerStation(InfinityStation):


    def __init__(self, observer, simulator: Simulator, distribution: Distribution,servers:int):
        self.queue=0
        self.servers=servers
        self.free_servers=servers
        super().__init__(observer, simulator, distribution)

    def client_arrival(self, event):
        if self.observer is not None:
            self.observer.client_arrival(event.time_stamp)
        if self._has_free_server():
            evt = Event(0, self, EventType.START_PROCESS)
            self.simulator.schedule_event(evt)
            self.free_servers -= 1
        else:
            self.queue += 1

    def client_departure(self, event):
        super().client_departure(event)
        if self.queue > 0:
            self.queue -= 1
            evt = Event(0, self, EventType.START_PROCESS) #Inizio lavoro per qualcuno in coda;
            self.simulator.schedule_event(evt)
        else:
            self.free_servers +=1
            if self.free_servers>self.servers:
                raise Exception("Too many servers")

    def reset(self):
        self.queue=0
        self.free_servers=self.servers

    def print_state(self):
        super().print_state()
        print("Len queue: " + str(self.queue))
        print("Serv status:" + str(self.free_servers))

    def _has_free_server(self):
        return self.free_servers>0


