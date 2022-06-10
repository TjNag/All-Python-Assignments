def tribonacci(n):
    if n == 1:
        print("0, ", end="")
    elif n == 2:
        print("0, 1, ", end="")
    elif n == 3:
        print("0, 1, 1, ", end="")
    else:
        count=3
        a=0
        b=1
        c=1
        print("0, 1, 1, ", end="")
        while(count<n):
            d=a+b+c
            count = count + 1
            a=b
            b=c
            c=d
            print(d, end="")
            print(", ", end="")
n=int(input("Enter the no. of terms: "))
print("Tribonacci sequence:")
tribonacci(n)