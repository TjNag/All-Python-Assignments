n=int(input("Enter a number: "))
s=0.0
for i in range(1,n+1):
    f=1
    for j in range(1, i+1):
        f=f*j
    s=s+i/f
print("Sum =",s)