class MalfunctionSheet:

    def __init__(self, id, train_run, date, repaired, cause):
        self.id = id
        self.train_run = train_run
        self.date = date
        self.repaired = repaired
        self.cause = cause

    id = 0
    train_run = 0
    date = ""
    repaired = False
    cause = ""

    def to_dict(self):
        return {
            'id': self.id,
            'train_run': self.train_run,
            'date': self.date,
            'repaired': self.repaired,
            'cause': self.cause
        }

