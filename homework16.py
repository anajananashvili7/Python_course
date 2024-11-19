from datetime import datetime

class Car:
    
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1  
    
    def car_info(self):
        
        print(f"მანქანა: ბრენდი - {self.brand}, მოდელი - {self.model}, წელი - {self.year}")
    
    def age_of_car(self):
        
        current_year = datetime.now().year
        return current_year - self.year

    @classmethod
    def total_cars(cls):
        
        print(f"მანქანების საერთო რაოდენობა: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
       
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი.")



car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2018)

car1.car_info()
print(f"მანქანის ასაკი: {car1.age_of_car()} წელი")
car2.car_info()
print(f"მანქანის ასაკი: {car2.age_of_car()} წელი")

Car.total_cars()  

electric_car = ElectricCar("Tesla", "Model S", 2020, 12)
electric_car.car_info()
electric_car.battery_info()
print(f"მანქანის ასაკი: {electric_car.age_of_car()} წელი")

Car.total_cars()  
