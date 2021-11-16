class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []


    def drive(self):
        return "Brum brum" 

    def passenger_count(self):
        return len(self.passengers)

    def pick_up (self, new_passenger):
        self.passengers.append(new_passenger)

    def drop_off (self, passenger):
        self.passengers.remove(passenger)
        
        