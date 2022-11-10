class Train:

    def __init__(self, id, type, capacity, seats):
        self.id = id
        self.type = type
        self.capacity = capacity
        self.seats = seats

    id = 0
    type = ""
    capacity = 0
    seats = 0

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'capacity': self.capacity,
            'seats': self.seats
        }
