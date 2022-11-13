class MalfunctionSheet:

    def __init__(self, id, train_run, date, repaired_at_track, cause, repairing_time):
        self.id = id
        self.train_run = train_run
        self.date = date
        self.repaired_at_track = repaired_at_track
        self.cause = cause
        self.repairing_time = repairing_time

    id = 0
    train_run = 0
    date = ""
    repaired_at_track = False
    cause = ""
    repairing_time = 0

    def to_dict(self):
        return {
            'id': self.id,
            'train_run': self.train_run,
            'date': self.date,
            'repaired': self.repaired_at_track,
            'cause': self.cause,
            'repairing_time': self.repairing_time
        }

