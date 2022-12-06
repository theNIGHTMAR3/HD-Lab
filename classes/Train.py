class Train:

    def __init__(self, id, type, cargo_type):
        self.id = id
        self.type = type
        self.cargo_type = cargo_type

    id = 0
    type = ""
    cargo_type = ""

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'cargo_type': self.cargo_type
        }
