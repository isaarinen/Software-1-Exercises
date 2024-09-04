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

cars = []
i = 1
while i < 11:
    car = Car()
    car.max_spd = random.randint(100, 200)
    car.reg_num = "ABC-" + str(i)
    cars.append(car)
    i += 1
race = True
while race == True:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        print(vars(car))
        if car.trvl_dist >= 10000:
            race = False


for car in cars:
    print(f"\nRegistration number: {car.reg_num}\nMaximum speed: {car.max_spd}km/h\nCurrent speed: {car.cur_spd}\nTravel distance: {car.trvl_dist}")
