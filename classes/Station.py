class Station:

    def __init__(self, id, station_name, city, renovation_year):
        self.id = id
        self.station_name = station_name
        self.city = city
        self.renovation_year = renovation_year

    id = 0
    station_name = ""
    city = ""

    # Slowly Changing Dimension - type 2 (SCD2)
    renovation_year = 0

    def to_dict(self):
        return {
            'id': self.id,
            'station_name': self.station_name,
            'city': self.city,
            'renovation_year': self.renovation_year
        }
