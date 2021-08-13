class Vehicle:
    def __init__(self):
    # Attributes
        pass 
    # Methods
    def go_forward(self, inc=1):
        self.pos += inc

    def go_backwards(self, inc=1):
        self.pos -= inc

    def paint_job(self, col="white"):
        self.color = col


class Sedan(Vehicle):
    def __init__(self, tires=4, color="silver", seats=5, year=2020, make="Toyota", model="Tacoma"):
        self.tires = tires
        self.color = color
        self.seats = seats
        self.year = year
        self.make = make
        self.model = model
        self.pos = 0
        self.name = "mycar"
 


class Truck(Vehicle):
    def __init__(self, tires=4, color="silver", seats=5, year=2020, make="Toyota", model="Tacoma", bed=5):
        self.bed = bed
        self.tires = tires
        self.color = color
        self.seats = seats
        self.year = year
        self.make = make
        self.model = model
        self.pos = 0
        self.name = "mycar"
 
    def offroad(self):
        self.pos += 7


hilux = Truck(color="red")
jedidiah = Truck(year=1997, color="dark red")

print(hilux.color)
print(jedidiah.color, jedidiah.year)

hilux.go_forward()
print(hilux.pos)

jedidiah.go_backwards(5)
print(jedidiah.pos)

hilux.paint_job()
print(hilux.color)
print(hilux.name)

hilux.offroad()
print("Hilux is at", hilux.pos)

soul = Sedan()
soul.go_forward(2)
print(soul.pos)
soul.offroad() #-- AttributeError
# print(soul.pos)
