# Project 3 by FA24-BCS-110
bday = int(input("Enter the date (DD) of your birth: "))
bmonth = int(input("Enter the month (MM) of your birth: "))
byear = int(input("Enter the year (YYYY) of your birth: "))
cday = int(input("Enter Today's date (DD): "))
cmonth = int(input("Enter the current month (MM): "))
cyear = int(input("Enter the current year (YYYY): "))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

years = cyear - byear
months = cmonth - bmonth
days = cday - bday

if days < 0:
    months -= 1
    days += days_in_month(bmonth, byear)

if months < 0:
    years -= 1
    months += 12

exact_age = f"{years} years, {months} months, and {days} days"
print(f"Your age is {exact_age}.")