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
x_month = input("Please enter your birth month (1 to 12 >> ")
x_day = input("please enter your dirth day (1 to 31)>> ")

i_month = int(x_month)
i_day = int(x_day)

if i_month < 10:
    xx_month = "0" + x_month
else:
    xx_month = x_month
    
if i_day < 10:
    xx_day = "0" + x_day
else:
    xx_day = x_day
    
x_mmdd = xx_month + xx_day

x_date = xx_month + " " + xx_day + " 2021"
d_born = datetime.datetime.strptime(x_date, '%m %d %Y').weekday()
x_weekday = calendar.day_name[d_born]

if x_mmdd in holidays.keys():
    x_holiday = holidays[x_mmdd]["holiday"]
    x_day = holidays[x_mmdd]["day"]
    print(f"Your 2021 brithday is on holiday {x_holiday} on {x_day}")
elif x_weekday == "Saturday" or x_weekday == "Sunday":
    print(f"Your 2021 birthday in on weekend {x_weekday}")
else:
    print(f"your 2021 birthday will be on a workday {x_weekday}")

