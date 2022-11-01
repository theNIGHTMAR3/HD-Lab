class Train:

    def __init__(self, id, type, carts, seats, capacity):
        self.id = id
        self.type = type
        self.carts = carts
        self.seats = seats
        self.capacity = capacity

    id = 0
    type = ""
    carts = 0
    seats = 0
    capacity = 0

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'carts': self.carts,
            'seats': self.seats,
            'capacity': self.capacity
        }
