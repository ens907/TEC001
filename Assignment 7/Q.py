#Q1-3

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
        distance_travelled = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance_travelled

car1 = Car("ABC-123", 142)

print("Registration number:", car1.registration_number)
print("Maximum speed:", car1.maximum_speed)
print("Current speed:", car1.current_speed)
print("Travelled distance:", car1.travelled_distance)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print("\nCurrent speed:", car1.current_speed)

car1.accelerate(-200)
print("Current speed after brake:", car1.current_speed)

#Q4

cars = []

for i in range(1, 11):
    registration = "ABC-" + str(i)
    max_speed = random.randint(150, 200)
    new_car = Car(registration, max_speed)
    cars.append(new_car)
    print("Created car:", registration, "max speed:", max_speed)

race_hours = 0

while True:
    race_hours = race_hours + 1
    
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
    
    someone_finished = False
    for car in cars:
        if car.travelled_distance >= 10000:
            someone_finished = True
    
    if someone_finished == True:
        break

print("\nRace finished after", race_hours, "hours")

print(f"\n{'Registration':<15} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<12}")

for car in cars:
    registration = car.registration_number
    max_speed = car.maximum_speed
    current_speed = car.current_speed
    distance = car.travelled_distance
    print(f"{registration:<15} {max_speed:<12} {current_speed:<15} {distance:<12}")