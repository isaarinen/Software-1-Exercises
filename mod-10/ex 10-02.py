class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.currentfloor = bottom_floor
    def floor_up(self):
        self.currentfloor += 1
        print(self.currentfloor)
    def floor_down(self):
        self.currentfloor -= 1
        print(self.currentfloor)
    def go_to_floor(self, floor):
        if floor < self.currentfloor and floor >= self.bottom_floor:
            while floor != self.currentfloor:
                self.floor_down()
        elif floor > self.currentfloor and floor <= self.top_floor:
            while floor != self.currentfloor:
                self.floor_up()
        elif floor == self.currentfloor:
            print(f'The elevator is on floor {floor} already.')
        else:
            print(f'Enter a valid floor between {self.bottom_floor} and {self.top_floor}')

class Building:
    elevators = []
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        i = 0
        while i < elevator_count:
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
            i += 1
    def run_elevator(self, elevator, destination):
        e = self.elevators[elevator]
        e.go_to_floor(destination)

b = Building(0, 20, 10)
b.run_elevator(5, 10)
b.run_elevator(1, 2)
b.run_elevator(2, 7)
b.run_elevator(5, 11)
