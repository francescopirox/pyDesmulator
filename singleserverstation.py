from event import Event, EventType
from infinityStation import InfinityStation


class SingleServerStation(InfinityStation):
    queue: int = 0
    server_free: bool = True

    def client_arrival(self, event):
        if self.observer is not None:
            self.observer.client_arrival(event.time_stamp)
        print("Cliente arrivato")
        if self.server_free:
            evt = Event(0, self, EventType.START_PROCESS)
            self.simulator.schedule_event(evt)
            self.server_free = False
        else:
            self.queue += 1

    def client_departure(self, event):
        super().client_departure(event)
        if (self.queue > 0):
            self.queue -= 1
            evt = Event(0, self, EventType.START_PROCESS)
            self.simulator.schedule_event(evt)
        else:
            self.server_free = True
