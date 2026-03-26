import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = self.current_speed + change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':15} {'Max Speed':12} {'Speed':15} {'Distance':12}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:15} {car.maximum_speed:12} {car.current_speed:15} {car.travelled_distance:12.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

#Create 10 cars in this part :D
race_cars = []
for i in range(1, 11):
    race_cars.append(Car("ABC-" + str(i), random.randint(150, 200)))

derby = Race("GDD", 8000, race_cars)

hours = 0
while derby.race_finished() == False:
    derby.hour_passes()
    hours = hours + 1
    
    if hours % 10 == 0:
        print(f"\nAt hour {hours}")
        derby.print_status()

print(f"\nRace finished after {hours} hours")
derby.print_status()