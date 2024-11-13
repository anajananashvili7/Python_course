#1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3) 

#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)  
print(book1 == book3)  



#3

class Car:
    def __new__(cls, brand, model, year):
        instance = super(Car, cls).__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = None
        self._model = None
        self._year = None

        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

   
    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str) and brand:
            self._brand = brand
        else:
            raise ValueError("Brand must be a non-empty string.")


    def get_model(self):
        return self._model

    def set_model(self, model):
        if isinstance(model, str) and model:
            self._model = model
        else:
            raise ValueError("Model must be a non-empty string.")

    def get_year(self):
        return self._year

    def set_year(self, year):
        if isinstance(year, int) and year > 1885: 
            self._year = year
        else:
            raise ValueError("Year must be an integer greater than 1885.")


try:
    car = Car("Toyota", "Camry", 2020)
    print(car.get_brand())  
    print(car.get_model())  
    print(car.get_year())   

    car.set_year(2018)    
    print(car.get_year())   

    car.set_year("2022")   
except ValueError as e:
    print(e)



