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

    def __init__(self, name, observer, simulator):
        self.observer = observer
        self.simulator = simulator
        self.simulator.station_bind(self)
        self.simulator.name = name


    def client_arrival(self, event):
        if self.observer is not None:
            self.observer.clientArrival()
        print("Cliente arrivato")
        evt = Event(event.time_stamp, self, self, EventType.START_PROCESS)
        self.simulator.schedule_event(evt)
        pass

    def client_departure(self, event):
        if self.observer is not None:
            self.observer.clientDeparture()
        print("Client Partito")
        evt = Event(event.time_stamp, self, self.next_station, EventType.ARRIVAL)
        self.simulator.schedule_event(evt)
        pass

    def service_client_start(self, event):
        if self.observer is not None:
            self.observer.client_service_start()
        print("cliente in lavorazione")

        evt = Event(event.time_stamp + 10, self, self, EventType.END_PROCESS)
        self.simulator.schedule_event(evt)

    def service_client_stop(self, event):
        print("cliente terminato")
        if self.observer is not None:
            self.observer.client_service_stop()
        evt = Event(event.time_stamp, self, self, EventType.DEPARTURE)
        self.simulator.schedule_event(evt)
