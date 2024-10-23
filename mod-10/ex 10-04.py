import random

class Car:
    cur_spd = 0
    trvl_dist = 0
    reg_num = ""
    max_spd = 0
    def accelerate(self, kmh):
        self.cur_spd += kmh
        if self.cur_spd > self.max_spd:
            self.cur_spd = self.max_spd
        if self.cur_spd < 0:
            self.cur_spd = 0
    def drive(self, hours):
        self.trvl_dist += self.cur_spd * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self, car):
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    def print_status(self, car):
        print(f"\nRegistration number: {car.reg_num}\nMaximum speed: {car.max_spd}km/h\nCurrent speed: {car.cur_spd}\nTravel distance: {car.trvl_dist}")
    def race_finished(self):
        for car in self.cars:
            if car.trvl_dist >= self.distance:
                return True

cars = []
i = 1
while i < 11:
    car = Car()
    car.max_spd = random.randint(100, 200)
    car.reg_num = "ABC-" + str(i)
    cars.append(car)
    i += 1

gdd = Race("Grand Demolition Derby", 8000, cars)
hour = 0
while True:
    for car in cars:
        gdd.hour_passes(car)
    hour += 1
    if gdd.race_finished() == True:
        for car in cars:
            gdd.print_status(car)
        break
    if hour % 10 == 0:
        for car in cars:
            gdd.print_status(car)

