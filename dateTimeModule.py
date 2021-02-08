import datetime
#1
myTime = datetime.time(13,41,20,1)
print(myTime.minute)
##prints minute counts in time that we input
print(myTime.hour)
#prints hour counts in time that we input
print(myTime)
#prints the complete time that we input

#2
myDate = datetime.date.today()
#stores the today's date to myDate var
print(myDate)
#prints today's date
print(myDate.year)
#prints current year
print(datetime.date.today())
#prints today's date
print(myDate.ctime())

#3
from datetime import datetime
print(datetime.today())
#prints current date and exact time


#4
from datetime import date
date1 = date(2003,11,12)
date2 = date(2004,11,12)
print(date2-date1)

#5
datetime1 = datetime(2020,11,3,13,00,11)
datetime2 = datetime(2021,11,4,23,00,10)
print(datetime2-datetime1)