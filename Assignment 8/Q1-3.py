class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is now on floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is now on floor {self.current}")

    def go_to_floor(self, target_floor):
        while self.current < target_floor:
            self.floor_up()
        while self.current > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, destination_floor):
        print(f"\nRunning Elevator {elevator_num}")
        self.elevators[elevator_num - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFire alert! Lets go to the bottom boys. This place is on fire!")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1} returning...")
            elevator.go_to_floor(self.bottom)
