class Vehicle:
    def __init__(self, brand, model, color, maxSpeed):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxSpeed = maxSpeed
    def start(self):
        print(
            f"Menyalakan kendaraan dengan brand dari {self.brand} model {self.model} warna {self.color}"
        )

    def stop(self):
        print(
            f"Mematikan kendaraan dengan brand dari {self.brand} model {self.model} warna {self.color}"
        )

    def turn(self):
        print(
            f"Maksimal kecepatan dari kendaraan brand {self.brand} model {self.model} warna {self.color} yaitu {self.maxSpeed}"
        )

class Truck(Vehicle):
    def __init__(self, brand, model, color, maxSpeed, loadCapacity):
        super().__init__(brand, model, color, maxSpeed)
        self.loadCapacity = loadCapacity
    def load(self):
         print(f"{self.brand} {self.model} {self.color} {self.maxSpeed} {self.loadCapacity}")
myTruck = Truck("Toyota", "Dyna", "kuning", 2000, 3000)
print(f"brand: {myTruck.brand}")
print(f"model : {myTruck.model}")
print(f"color : {myTruck.color}")
print(f"kecemaks : {myTruck.maxSpeed} KM/j" )
print(f"muatan : {myTruck.loadCapacity} kg")
myTruck.start()
myTruck.load()
myTruck.stop()