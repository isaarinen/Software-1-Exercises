sex = input('What is your biological gender? (male/female) ')
gl = input('What is your hemoglobin value? ')
if sex == 'male':
    if int(gl) < 134:
        print('Your hemoglobin value is low.')
    elif int(gl) > 167:
        print('Your hemoglobin value is high.')
    else:
        print('Your hemoglobin value is normal.')
elif sex == 'female':
    if int(gl) < 117:
        print('Your hemoglobin value is low.')
    elif int(gl) > 155:
        print('Your hemoglobin value is high.')
    else:
        print('Your hemoglobin value is normal.')
else:
    print('Invalid gender input.')