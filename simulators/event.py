from enum import Enum

class EventType(Enum):
    NULL = 0
    START = 1
    DEPARTURE = 2
    ARRIVAL = 3
    STOP = 4
    START_PROCESS = 5
    END_PROCESS = 6
# Classe che gestisce gli eventi e le sue tipologie

class Event:
    time_stamp: int = 0
    destination = None
    type = EventType.NULL

    def __init__(self, delay: int, destination, event_type: EventType):
        self.delay=delay
        self.time_stamp = 0
        self.destination = destination
        self.type = event_type

    def __str__(self):
        eventtype:str =""
        if(self.type == EventType.ARRIVAL):
            eventtype="Client arrival "
        elif(self.type == EventType.DEPARTURE):
            eventtype="Client departure"
        elif(self.type == EventType.START_PROCESS):
            eventtype="Client service start"
        elif(self.type == EventType.END_PROCESS):
            eventtype="Client service stop"
        else:
            eventtype="Process"

        if self.destination is not None:
            return "Time: "+str(self.time_stamp)+" "+eventtype+" "+str(self.destination)
        else:
            return "Time: " + str(self.time_stamp) + " " + eventtype + " "
    def __cmp__(self, other):
        if self.time_stamp > other.time_stamp:
            return 1
        elif self.time_stamp < other.time_stamp:
            return -1
        return 0

    def __eq__(self, o: object) -> bool:
        if isinstance(o,Event):
            return self.time_stamp == o.time_stamp and self.type == o.type

    def __lt__(self, other):
        return self.time_stamp>other.time_stamp

    def add_time_stamp(self, actual_time: int):
        self.time_stamp = self.delay + actual_time
