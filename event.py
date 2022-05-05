
class Event:
    time_stamp = 0
    arrival_station = None
    departure_station = None

    def __init__(self, time_stamp,departure_station, arrival_station):
        self.time_stamp=time_stamp
        self.departure_station=departure_station
        self.arrival_station=arrival_station

    def __str__(self):
        return str(self.arrival_station)+str(self.departure_station)+self.time_stamp


    def __cmp__(self, other):
        return self.compare(other)

    def compare(self, evt_2):
        if self.time_stamp > evt_2.time_stamp:
            return 1
        if self.time_stamp < evt_2.time_stamp:
            return -1
        return 0