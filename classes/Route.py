class Route:

    def __init__(self, id, id_station_start, id_station_end):
        self.id = id
        self.id_station_start = id_station_start
        self.id_station_end = id_station_end


    id = 0
    id_station_start = 0
    id_station_end = 0


    def to_dict(self):
        return {
            'id': self.id,
            'id_station_start': self.id_station_start,
            'id_station_end': self.id_station_end
        }