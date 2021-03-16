y = float(input('Enter the angle of rotation of the hour hand: '))

if y<0 or y >360:
    print('Wrong number')
else:
    hours = y // 30
    minutes = y % 30 // 0.5
    print("%.0f" % hours, 'hours', "%.0f" % minutes, 'minutes')