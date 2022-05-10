from enum import Enum


class EventType(Enum):
    NULL = 0
    START = 1
    DEPARTURE = 2
    ARRIVAL = 3
    STOP = 4
    START_PROCESS = 5
    END_PROCESS = 6


class Event:
    time_stamp: int = 0
    destination = None
    type = EventType.NULL

    def __init__(self, time_stamp: int, destination, event_type):
        self.time_stamp = time_stamp
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


        return "Time: "+str(self.time_stamp)+" "+eventtype+" "+str(self.destination)

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
        return self.time_stamp-other.time_stamp

    def add_time(self, delay: int):
        self.time_stamp = self.time_stamp + delay
