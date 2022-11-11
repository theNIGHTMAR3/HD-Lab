class Malfunction:

    def __init__(self, id, train_run, carts, date):
        self.id = id
        self.train_run = train_run
        self.date = date

    id = 0
    train_run = 0
    date = ""

    def to_dict(self):
        return {
            'id': self.id,
            'train_run': self.train_run,
            'date': self.date,
        }

