a= float(input("Enter a number: ")) 
b= float(input("Enter a number: "))
c= float(input("Enter a number: "))
if a>=b and a>=c:
    m=a
elif b>=a and b>=c:
    m=b
else:
    m=c
print("Largest of 3 number is :",m)
