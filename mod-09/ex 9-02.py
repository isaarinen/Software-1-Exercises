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

        

newcar = Car()
newcar.reg_num = 'ABC-123'
newcar.max_spd = 142
print(f"Current speed: {newcar.cur_spd}\nTravel distance: {newcar.trvl_dist}\nRegistration number: {newcar.reg_num}\nMaximum speed: {newcar.max_spd}km/h")
newcar.accelerate(30)
newcar.accelerate(70)
newcar.accelerate(50)
print(f'Current speed: {newcar.cur_spd}km/h')
newcar.accelerate(-200)
print(f'Current speed: {newcar.cur_spd}km/h')