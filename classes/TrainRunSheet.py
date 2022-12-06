class TrainRunSheet:

    def __init__(self, id, items_mass, seats_taken, seats_total, capacity, id_driver, date_of_arrival, delay, if_malfunction_happened):
        self.id = id
        self.items_mass = items_mass
        self.seats_taken = seats_taken
        self.seats_total = seats_total
        self.capacity = capacity
        self.id_driver = id_driver
        self.date_of_arrival = date_of_arrival
        self.delay = delay
        self.if_malfunction_happened = if_malfunction_happened

    id = 0
    items_mass = 0
    seats_taken = 0
    seats_total = 0
    capacity = 0
    id_driver = 0
    date_of_arrival = ""
    delay = 0
    if_malfunction_happened = False

    def to_dict(self):
        return {
            'id': self.id,
            'items_mass': self.items_mass,
            'seats_taken': self.seats_taken,
            'seats_total': self.seats_total,
            'capacity': self.capacity,
            'id_driver': self.id_driver,
            'date_of_arrival': self.date_of_arrival,
            'delay': self.delay,
            'if_malfunction_happened': self.if_malfunction_happened

        }
