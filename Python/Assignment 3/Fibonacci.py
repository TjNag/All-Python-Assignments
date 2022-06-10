n=int(input("Enter the no. of terms: "))
print("Fibonacci sequence:")
if n == 1:
    print("0, ", end="")
elif n == 2:
    print("0, 1, ", end="")
else:
    count=2
    a=0
    b=1
    print("0, 1, ", end="")
    while(count<n):
        c=a+b
        count = count + 1
        a=b
        b=c
        print(c, end=", ")