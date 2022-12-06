class Malfunction:

    def __init__(self, id, id_train_run, date):
        self.id = id
        self.id_train_run = id_train_run
        self.date = date

    id = 0
    id_train_run = 0
    date = ""

    def to_dict(self):
        return {
            'id': self.id,
            'train_run': self.id_train_run,
            'date': self.date,
        }

