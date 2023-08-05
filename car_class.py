class Car:
    car_type = "Honda Civic"

    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

blue_car = Car(color = "blue", miles = 20_000)
red_car = Car(color="red",miles=30_000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.miles:,} miles")