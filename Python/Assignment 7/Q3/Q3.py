#Define a factorial function in a user-defined module “MyFact” and use command line argument to find the factorial value of the input.

import MyFact

n=int(input("Enter a number : "))
f=MyFact.factorial(n)
print("Factorial :",f)