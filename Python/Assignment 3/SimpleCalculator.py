from cmath import sqrt

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
print("Press '1' to add")
print("Press '2' to substract")
print("Press '3' to multiply")
print("Press '4' to divide")
print("Press '5' to square root")
ch = int(input("Enter your choice : "))
if ch==1:
    print("Sum =", a+b)
elif ch==2:
    print("Difference =", a-b)
elif ch==3:
    print("Product =",a*b)
elif ch==4:
    print("Division =",a/b)
elif ch==5:
    print("Square root of",a,"=",sqrt(a))
    print("Square root of",b,"=",sqrt(b))
else:
    print("Wrong choice !")