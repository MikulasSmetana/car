class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    def accelerate(self, increase):
        self.speed += increase
        print(f"Auto nyní jede rychlostí {self.speed} km/h")

    def breakk(self, decrease):
        if(self.speed >= decrease):
            self.speed -= decrease
        else:
            self.speed = 0
        print(f"Auto nyní jede rychlostí {self.speed} km/h")
# vytvoření objektu
auto1 = Car("BMW","i8",2022)
print(auto1.brand)
print(auto1.model)
print(auto1.year)

auto1.accelerate(50)
auto1.breakk(55)