class Vehicle:
    def __init__(self, brand, doors, wheels=4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels



    def car_greeting(self, local_slang):
        print(f'{local_slang}, im your new car. My name is {self.brand}. I have {self.wheels} wheels')


vah1 = Vehicle('Mazda', 4,3)
print(vah1.wheels)
vah1.car_greeting('Sup')

vah2 = Vehicle('BMW', 2)


class Car:
    brand = 'Honda'


car1 = Car()
print(car1.brand)
car2 = Car()
print(car2.brand)
