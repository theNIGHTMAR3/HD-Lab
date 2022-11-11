class TimeClass:

    def __init__(self, id, year, month_name, day_number, day_in_week_number, day_in_week_name):
        self.id = id
        self.year = year
        self.month_name = month_name
        self.day_number = day_number
        self.day_in_week_number = day_in_week_number
        self.day_in_week_name = day_in_week_name

    id = 0
    year = 0
    month_name = ""
    month_number = 0
    day_number = 0
    day_in_week_number = 0
    day_in_week_name = ""

    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'month_name': self.month_name,
            'day_number': self.day_number,
            'day_in_week_number': self.day_in_week_number,
            'day_in_week_name' : self.day_in_week_name
        }
