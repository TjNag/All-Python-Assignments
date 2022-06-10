#Write a Python program that defines a function large in a module which will be used to find larger of two values and called from code in another module.

import Larger

a=int(input("Enter two numbers :\n"))
b=int(input())

max = Larger.large(a, b)

print("Largest of two numbers : ", max)