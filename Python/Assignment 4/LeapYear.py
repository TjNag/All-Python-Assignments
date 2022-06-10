def LeapYear(n):
    if(n%4==0):
        if(n%100==0 and n%400==0):
            return 1
        elif(n%100==0):
            return 0
        else:
            return 1
    else:
        return 0
yr=int(input("Enter a year: "))
x=LeapYear(yr)
if(x==1):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")