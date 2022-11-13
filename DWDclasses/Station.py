
class Station:

    def __init__(self, id, station_name, city, in_renovation):
        self.id = id
        self.station_name = station_name
        self.city = city
        self.in_renovation = in_renovation

    id = 0
    station_name = ""
    city = ""
    in_renovation = False

    def to_dict(self):
        return {
            'id': self.id,
            'station_name': self.station_name,
            'city': self.city,
            'in_renovation': self.in_renovation
        }