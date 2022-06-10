'''
year 4
year 100, year 400
 '''
n=int(input("Enter any year:"))
if (n%4==0):
    if n%100==0 and n%400==0:
        print("Leap Year")
    elif n%100==0:
        print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")