import sys
n=int(sys.argv[1])
c=0
while (n!=0):
    n=n//10
    c=c+1
print("No. of digits:",c)