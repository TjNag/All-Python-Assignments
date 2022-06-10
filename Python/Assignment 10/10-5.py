fibonacci = {}

def fibo(N):
    if N<=1:
        return N
    return fibo(N-1)+fibo(N-2) 


n = int(input("Enter no. of terms : "))

for i in range(0, n):
    fibonacci[i] = fibo(i)

print(fibonacci)