#Write a Python program that finds whether a given Character is present in a
#String or not. In case it is present, it prints the Index at which it is
#present. (Don't use built in function).
str = input("Enter a String: ")
ch = input("Enter the character to check presence: ")
ind=-1
for i in range(0,len(str)):
    if str[i] == ch:
        ind=i
        break
if ind==-1:
    print(f"{ch} is not present in {str}")
else:
    print(f"{ch} is present in {str} at {ind}")