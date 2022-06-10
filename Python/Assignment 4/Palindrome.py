def Reverse(n):
    rev=0
    while(n!=0):
        dig=n%10
        n=n//10
        rev=rev*10+dig
    return rev
n=int(input("Enter a number: "))
r=Reverse(n)
if r==n:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")