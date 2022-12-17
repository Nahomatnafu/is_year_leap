"""
Written by Nahom Atnafu
Date: 12/11/2022

"""

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It's a leap year.")
            else:
                print("Not a leap year.")
        else:
            print("It's a leap year.")
    else:
        print("Not a leap year.")


year = int(input('Enter a year: '))
is_leap(year)
