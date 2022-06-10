#from os import system
#import os
#os.system('cls')

n=int(input("Enter any number: "))
n1=n
rev=0
while(n1>0):
    dig=n1%10
    rev=rev*10+dig
    n1=n1//10
if rev == n:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
