def Tribonacci(n):
    if n<=1:
        return n
    elif n==2:
        return n-1
    else:
        return (Tribonacci(n-3) + Tribonacci(n-2) + Tribonacci(n-1))

n = int(input("Enter no. of terms: "))
if n<=0:
    print("Bhag!")
else:
    for i in range(n):
        print(f"{Tribonacci(i)}, ", end="")