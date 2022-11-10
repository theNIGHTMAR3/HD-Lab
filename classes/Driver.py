class Driver:
    id = 0
    nameAndSurname = ""
    gender = ""
    PESEL = ""

    def __init__(self, id, nameAndSurname, gender, PESEL):
        self.id = id
        self.nameAndSurname = nameAndSurname
        self.gender = gender
        self.PESEL = PESEL


    def to_dict(self):
        return {
            'id': self.id,
            'nameAndSurname': self.nameAndSurname,
            'gender': self.gender,
            'PESEL': self.PESEL
        }
