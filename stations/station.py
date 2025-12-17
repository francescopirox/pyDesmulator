from simulators.event import Event, EventType
from observers import Observer
from simulators.simulator import Simulator

# Classe che definisce una stazione che mette a disposizione funzionalità limitate
class Station:

    def __init__(self, observer:Observer, simulator:Simulator):
        self.observer:Observer = observer
        self.simulator:Simulator = simulator
        self.simulator.station_bind(self)
        self.next_station = None
        self.name=""

    def __init__(self, name: str, observer:Observer, simulator:Simulator):
        self.observer = observer
        self.simulator = simulator
        self.simulator.station_bind(self)
        self.next_station = None
        self.name = name

    #Metodo invocato dal simulatore
    def client_arrival(self, event:Event):
        if self.observer is not None: ##generico non usare
            self.observer.client_arrival(event.time_stamp) #LOG
        evt = Event(0,self, EventType.START_PROCESS)
        self.simulator.schedule_event(evt)

    #Metodo Invocato dal simulatore
    def client_departure(self, event):
        if self.observer is not None:
            self.observer.client_departure(event.time_stamp)
        evt = Event(0,self.next_station, EventType.ARRIVAL)
        self.simulator.schedule_event(evt)


    def service_client_start(self, event):
       pass

    def service_client_stop(self, event):
        if self.observer is not None:
            self.observer.client_service_stop(event.time_stamp)
        evt = Event(0, self, EventType.DEPARTURE)
        self.simulator.schedule_event(evt)

    def __str__(self) -> str:
        return self.name

    def reset(self):
        pass

    #Stampa traccia
    #Deprecato
    def print_state(self):
        print("Stazione: " + self.name)


