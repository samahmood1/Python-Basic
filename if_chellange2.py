#!/usr/bin/env python3
import datetime
import calendar

holidays = {
    "0101": {"day": "Friday", "holiday": "New Year’s Day"},
    "0118": {"day": "Monday", "holiday": "Martin Luther King, Jr. Day"},
    "0215": {"day": "Monday", "holiday": "President’s Day"},
    "0531": {"day": "Monday", "holiday": "Memorial Day"},
    "0704": {"day": "Sunday", "holiday": "Independence Day"},
    "0705": {"day": "Monday", "holiday": "Independence Day (observed)"},
    "0906": {"day": "Monday", "holiday": "Labor Day"},
    "1011": {"day": "Monday", "holiday": "Columbus Day"},
    "1111": {"day": "Thursday", "holiday": "Veterans Day"},
    "1125": {"day": "Thursday", "holiday": "Thanksgiving Day"},
    "1224": {"day": "Friday", "holiday": "Christmas Day (observed)"},
    "1225": {"day": "Saturday", "holiday": "Christmas Day"},
    "1231": {"day": "Friday", "holiday": "New Year’s Day (observed)"}
}

x_name = input("Please enter your name >> ")

l_done = False
while not l_done:
    x_month = input("Please enter your birth month (1 to 12 >> ")
    if x_month.isdigit():
        i_month = int(x_month)
        if i_month > 0 and i_month <= 12:
            l_done = True
        else:
            print("You entered a wrong number for the month, please try again")
    else:
        print("You entered a non-munber for the month, please try again")
        
if i_month in [1,3,5,7,8,10,12]:
    i_max_day = 31
elif i_month == 2:
    i_max_day = 29
else:
    i_max_day = 30
    
l_done = False
while not l_done:
    x_day = input(f"please enter your dirth day (1 to {i_max_day})>> ")
    if x_day.isdigit():
        i_day = int(x_day)
        if i_day > 0 and i_day <= i_max_day:
            l_done = True
        else:
            print("You entered a wrong number for the day, please try again")
    else:
        print("You entered a non-munber for the day, please try again")

if i_month < 10:
    xx_month = "0" + x_month
else:
    xx_month = x_month
    
if i_day < 10:
    xx_day = "0" + x_day
else:
    xx_day = x_day
    
x_mmdd = xx_month + xx_day

if x_mmdd != "0229":
    x_date = xx_month + " " + xx_day + " 2021"
    d_born = datetime.datetime.strptime(x_date, '%m %d %Y').weekday()
    x_weekday = calendar.day_name[d_born]

if x_mmdd in holidays.keys():
    x_holiday = holidays[x_mmdd]["holiday"]
    x_day = holidays[x_mmdd]["day"]
    print(f"Your 2021 brithday is on holiday {x_holiday} on {x_day}")
elif x_mmdd == "0229":
    print("Sorry you don't have a birthday this year, please wait three more years for your birthday")
elif x_weekday == "Saturday" or x_weekday == "Sunday":
    print(f"Your 2021 birthday in on weekend {x_weekday}")
else:
    print(f"your 2021 birthday will be on a workday {x_weekday}")

