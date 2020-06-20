import datetime

def get_date_time():
    while True:
        date = input("Input date dd/mm/yyyy ")
        time = input("Input time hh:mm ")
        day = date[:2]
        month = date[3:5]
        year = date[6:10]
        hour = time[:2]
        minute = time[3:5]
        try:
            dt = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
            return dt
        except ValueError as e:
            print(e)
            
print(get_date_time())
