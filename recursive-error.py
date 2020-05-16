def inputtime():
    time = input('time hh:mm ')
    if len(time) < 5 or len(time) > 5:
        print('ERROR: no of chars')
        time = inputtime()
    elif int(time[0:2]) > 23:
        print('ERROR: Hour')
        time = inputtime()
    elif int(time[3:5]) > 59:
        print('ERROR: Mins')
        time = inputtime()
    return time

time = inputtime()
print(time)
