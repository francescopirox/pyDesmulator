from .event import Event, EventType

# classe che definisce un simulatore

class Simulator:
    time:int = 0
    end_time:int = 0
    event_list = []
    station_list = []
    trace: bool= True

    def __init__(self, end_time) -> None:
        super().__init__()
        self.end_time = end_time

    # si occupa di aggiungere al "Calendario" gli eventi in ordine
    def schedule_event(self, event: Event):
        event.add_time(self.time)
        self.event_list.append(event)
        self.event_list.sort()

    #si occupa di processare gli eventi  della simulazione
    def process(self):
        while self.time < self.end_time:
            #lista eventi vuota
            if len(self.event_list) == 0:
                raise Exception("Simulation DeadLock")
            evt = self.event_list.pop()
            if evt is None:
                raise Exception("evt is none")
            if evt.time_stamp != self.time:
                raise Exception("time error")
            if evt.type is not EventType.NULL and evt.destination is not None:
                if self.trace:
                    print(evt)
                if evt.type is EventType.DEPARTURE:
                    evt.destination.client_departure(evt)

                if evt.type is EventType.ARRIVAL:
                    evt.destination.client_arrival(evt)

                if evt.type is EventType.START_PROCESS:
                    evt.destination.service_client_start(evt)

                if evt.type is EventType.END_PROCESS:
                    evt.destination.service_client_stop(evt)

            self.time_advance()

    #Calcola l'avanzamento temporale o mantiene
    def time_advance(self):
        if len(self.event_list) == 0:
            raise Exception("Simulation DeadLock")
        #self.event_list.sort()
        next_evt = self.event_list[-1]
        if next_evt.time_stamp > self.time:
            self.time = next_evt.time_stamp
        if self.trace:
            print("time: "+str(self.time))

    #Permette di fare partire la simulazione saltando al primo istante
    def start_simulation(self):
        self.time_advance()
        self.process()

    #Permette di fare continuare la simulazione
    def resume_simulation(self,time):
        self.end_time += time
        self.time_advance()
        self.process()

    # Effettua il bind tra simulazione e stazioni che ne fanno parte
    def station_bind(self, station):
        self.station_list.append(station)

    def reset(self):
        self.time: int = 0
        self.event_list = []
        for station in self.station_list:
            station.reset()