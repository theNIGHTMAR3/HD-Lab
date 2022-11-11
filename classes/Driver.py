class Driver:
    PESEL = ""
    name = ""
    surname = ""
    gender = ""

    def __init__(self, PESEL, name, surname, gender):
        self.PESEL = PESEL
        self.name = name
        self.surname = surname
        self.gender = gender

    def to_dict(self):
        return {
            'PESEL': self.PESEL,
            'name': self.name,
            'surname': self.surname,
            'gender': self.gender,
        }
