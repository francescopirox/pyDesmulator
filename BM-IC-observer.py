from observer import Observer


class BMICobserver(Observer):

    def client_arrival(self, time):
        super().client_arrival(time)

    def client_departure(self, time):
        super().client_departure(time)

    def client_service_start(self, time):
        super().client_service_start(time)

    def client_service_stop(self, time):
        super().client_service_stop(time)