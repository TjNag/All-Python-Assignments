#Write a Python program inside a user define module that accepts three integers and returns True if they are sorted,
#otherwise it returns False. Return this True and False in another source code.

import SortCheck

a=int(input("Enter three numbers to check if they are sorted:\n"))
b=int(input())
c=int(input())

print(SortCheck.sort(a, b, c))