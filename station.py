from event import Event, EventType


class Station:
    next_station = None
    observer = None
    simulator = None
    name = ""

    def __init__(self, observer, simulator):
        self.observer = observer
        self.simulator = simulator
        self.simulator.station_bind(self)

    def __init__(self, name:str, observer, simulator):
        self.observer = observer
        self.simulator = simulator
        self.simulator.station_bind(self)
        self.simulator.name = name


    def client_arrival(self, event):
        if self.observer is not None:
            self.observer.clientArrival(event.time_stamp)
        print("Cliente arrivato")
        evt = Event(0, self, self, EventType.START_PROCESS)
        self.simulator.schedule_event(evt)
        pass

    def client_departure(self, event):
        if self.observer is not None:
            self.observer.clientDeparture(event.time_stamp)
        print("Client Partito")
        evt = Event(0, self, self.next_station, EventType.ARRIVAL)
        self.simulator.schedule_event(evt)
        pass

    def service_client_start(self, event):
        if self.observer is not None:
            self.observer.client_service_start(event.time_stamp)
        print("cliente in lavorazione")


    def service_client_stop(self, event):
        print("cliente terminato")
        if self.observer is not None:
            self.observer.client_service_stop(event.time_stamp)
        evt = Event(0, self, self, EventType.DEPARTURE)
        self.simulator.schedule_event(evt)
