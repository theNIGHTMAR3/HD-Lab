class TrainRunSheet:

    def __init__(self, id, items_mass, items_type, seats_taken):
        self.id = id
        self.items_mass = items_mass
        self.items_type = items_type
        self.seats_taken = seats_taken

    id = 0
    items_mass = 0
    items_type = 0
    seats_taken = 0

    def to_dict(self):
        return {
            'id': self.id,
            'items_mass': self.items_mass,
            'items_type': self.items_type,
            'seats_taken': self.seats_taken
        }
