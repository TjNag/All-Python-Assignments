#Write a Python program to print date and time using time module and print the calendar of a particular month.

import datetime
import calendar

dt = datetime.datetime.now()
print(f"Date = {dt.day}-{dt.month}-{dt.year}")
print(f"Time = {dt.hour}:{dt.minute}:{dt.second}")

print("\nView Calendar :")
y = int(input("Input the year : "))
m = int(input("Input the month number : : "))
print(calendar.month(y, m))