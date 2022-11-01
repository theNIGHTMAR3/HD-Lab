
class Station:

    def __init__(self, id, station_name, city):
        self.id = id
        self.station_name = station_name
        self.city = city

    id = 0
    station_name = ""
    city = ""

    def to_dict(self):
        return {
            'id': self.id,
            'station_name': self.station_name,
            'city': self.city
        }