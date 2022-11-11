class Malfunction:

    def __init__(self, id, train_run, date, time, cause, repaired, repairing_time):
        self.id = id
        self.train_run = train_run
        self.date = date
        self.time = time
        self.cause = cause
        self.repaired = repaired
        self.repairing_time = repairing_time

    id = 0
    train_run = 0
    date = ""
    time = ""
    cause = ""
    repaired = False
    repairing_time = 0

    def to_dict(self):
        return {
            'id': self.id,
            'train_run': self.train_run,
            'date': self.date,
            'time': self.time,
            'cause': self.cause,
            'repaired': self.repaired,
            'repairing_time': self.repairing_time
        }

