class DateClass:

    def __init__(self, id, hour, minute):
        self.id = id
        self.year = hour
        self.minute = minute

    id = 0
    hour = 0
    minute = ""

    def to_dict(self):
        return {
            'id': self.id,
            'year': self.hour,
            'month_name': self.minute
        }
