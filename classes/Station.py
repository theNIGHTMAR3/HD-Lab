class Station:

    def __init__(self, id, station_name, city, in_renovation, start_date, end_date, is_current):
        self.id = id
        self.station_name = station_name
        self.city = city
        self.in_renovation = in_renovation
        self.start_date = start_date
        self.end_date = end_date
        self.is_current = is_current

    id = 0
    station_name = ""
    city = ""
    in_renovation = False

    # Slowly Changing Dimension - type 2 (SCD2)
    start_date = 0
    end_date = 0
    is_current = 0

    def to_dict(self):
        return {
            'id': self.id,
            'station_name': self.station_name,
            'city': self.city,
            'in_renovation': self.in_renovation,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'is_current': self.is_current
        }
