import datetime

def get_date_time():
    while True:
        date = input("Input date dd/mm/yyyy ")
        time = input("Input time hh:mm ")
        day = int(date[:2])
        month = int(date[3:5])
        year = int(date[6:10])
        hour = int(time[:2])
        minute = int(time[3:5])
        try:
            dt = datetime.datetime(year,month,day,hour,minute)
            return dt
        except ValueError as e:
            print(e)
            
print(get_date_time())
