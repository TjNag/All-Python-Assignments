n=int(input("Enter any number: "))
c=0
for i in range(2,n//2):
    if(n%i==0):
        c=c+1
if(c==0):
    print("Prime Number")
else:
    print("Not Prime Number")