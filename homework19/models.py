class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def to_dict(self):
        return {"city": self.city, "street": self.street}


class Student:
    row_id_counter = 1

    def __init__(self, name, mark, address):
        self.row_id = Student.row_id_counter
        Student.row_id_counter += 1
        self.name = name
        self.mark = mark
        self.address = address

    def to_dict(self):
        return {
            "row_id": self.row_id,
            "name": self.name,
            "mark": self.mark,
            "address": self.address.to_dict(),
        }
