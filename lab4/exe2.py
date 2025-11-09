class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"Транспортное средство - Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

vehicle1 = Vehicle("Porsche", "911")
car1 = Car("Audi", "A7", "Бензин")
car2 = Car("Peugeot", "308", "Бензин")

print("    Информация о транспортных средствах    ")
print(vehicle1.get_info())
print(car1.get_info())
print(car2.get_info())
