import datetime

#Date[date,time,datetime,timezone,timedelta

#date
today_date = datetime.date(2020,8,13)
print(today_date)
today = datetime.date.today()  #to view current date
print(today)
print(today.year)
print(today.month)

#weekday
print(today.weekday())#0-MONDAY , 1-TUESDAY
print(today.isoweekday())#1-MONDAY , 2-TUESDAY

#timedelta-diff b/w 2days
#timedelta+day

today = datetime.date.today()
today_delta = datetime.timedelta(days=5)
print(today)
print(today+today_delta)
print(today-today_delta)

#find no of days passed in this year
new_year = datetime.date(2020,1,1)
print("no of days passes",today-new_year)
print("no of days passes",(today-new_year).days)

#time = h/m/s/microsec 
my_time = datetime.time(8,7,59,567891)
print(my_time)
#date+time
my_day = datetime.datetime(2020,12,7,8,7,59,567891)
print(my_day)
