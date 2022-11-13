class Train:

    def __init__(self, id, type, seats, capacity):
        self.id = id
        self.type = type
        self.seats = seats
        self.capacity = capacity

    id = 0
    type = ""
    seats = 0
    capacity = 0

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'seats': self.seats,
            'capacity': self.capacity
        }
