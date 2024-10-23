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
        if floor < self.currentfloor:
            while floor != self.currentfloor:
                self.floor_down()
        elif floor > self.currentfloor:
            while floor != self.currentfloor:
                self.floor_up()

h = Elevator(-11, 11)
h.go_to_floor(5)
