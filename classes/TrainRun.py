class TrainRun:
    id = 0
    id_train = 0
    id_route = 0
    id_driver = 0
    id_date_arrival = 0
    id_time_planned_arrival = 0
    id_time_arrival_real = 0

    def __init__(self, id, planned_arrival, real_arrival, id_train, id_route, id_pesel):
        self.id = id
        #self.planned_departure = planned_departure
        self.planned_arrival = planned_arrival
        #self.real_departure = real_departure
        self.real_arrival = real_arrival
        self.id_train = id_train
        self.id_route = id_route
        self.id_pesel = id_pesel

    def to_dict(self):
        return {
            'id': self.id,
            #'planned_departure': self.planned_departure,
            'planned_arrival': self.planned_arrival,
            #'real_departure': self.real_departure,
            'real_arrival': self.real_arrival,
            'id_train': self.id_train,
            'id_route': self.id_route,
            'id_pesel': self.id_pesel,
        }




