class Car:
    cur_spd = "0"
    trvl_dist = "0"
    reg_num = ""
    max_spd = ""

newcar = Car()
newcar.reg_num = 'ABC-123'
newcar.max_spd = '142 km/h'
print(f"Current speed: {newcar.cur_spd}\nTravel distance: {newcar.trvl_dist}\nRegistration number: {newcar.reg_num}\nMaximum speed: {newcar.max_spd}km/h")
