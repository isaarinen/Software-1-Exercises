import random

class Car:
    def __init__(self, reg_num, max_spd):
        self.cur_spd = 0
        self.trvl_dist = 0
        self.reg_num = reg_num
        self.max_spd = max_spd
    def accelerate(self, kmh):
        self.cur_spd += kmh
        if self.cur_spd > self.max_spd:
            self.cur_spd = self.max_spd
        if self.cur_spd < 0:
            self.cur_spd = 0
    def drive(self, hours):
        self.trvl_dist += self.cur_spd * hours
class ElectricCar(Car):
    def __init__(self,reg_num,max_spd,battery):
        Car.__init__(self, reg_num, max_spd)
        self.battery = battery
class GasolineCar(Car):
    def __init__(self, reg_num, max_spd, gas_tank):
        Car.__init__(self, reg_num, max_spd)
        self.gas_tank = gas_tank

ecar = ElectricCar('ABC-15', 180, 52.5)
gcar = GasolineCar('ACD-123', 165, 32.3)

ecar.accelerate(150)
gcar.accelerate(120)

ecar.drive(3)
gcar.drive(3)
print(f'Electronic Car kilometers: {ecar.trvl_dist}')
print(f'Gasoline Car kilometers: {gcar.trvl_dist}')