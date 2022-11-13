class TrainRun:
    id = 0
    id_train = 0
    id_route = 0
    id_driver = 0
    id_date_arrival = 0
    id_time_arrival_planned = 0
    id_time_arrival_real = 0
    delay = 0
    items_mass = 0
    items_type = 0
    seats_taken = 0

    def __init__(self, id, id_train, id_route, id_driver,
                 id_date_arrival, id_time_arrival_planned, id_time_arrival_real,
                 delay, items_mass, items_type, seats_taken):
        self.id = id
        self.id_train = id_train
        self.id_route = id_route
        self.id_driver = id_driver
        self.id_date_arrival = id_date_arrival
        self.id_time_arrival_planned = id_time_arrival_planned
        self.id_time_arrival_real = id_time_arrival_real
        self.delay = delay
        self.items_mass = items_mass
        self.items_type = items_type
        self.seats_taken = seats_taken

    def to_dict(self):
        return {
            'id': self.id,
            'id_train': self.id_train,
            'id_route': self.id_route,
            'id_driver': self.id_driver,
            'id_date_arrival': self.id_date_arrival,
            'id_time_arrival_planned': self.id_time_arrival_planned,
            'id_time_arrival_real': self.id_time_arrival_real,
            'delay': self.delay,
            'items_mass': self.items_mass,
            'items_type': self.items_type,
            'seats_taken': self.seats_taken
        }
