#Febuary_Days.py
#Ryan Carroll
#CIS 115 NLE01
#is a year a leap year?

print("This program tests if a year is a leap year or not.")

leap_year = False
year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    leap_year = True

elif year % 4 == 0 and year % 100 != 0:
    leap_year = True

if leap_year:
    print(f"{year}: It's a leap year.")
else:
    print(f"{year}: It's not a leap year.")
