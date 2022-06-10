str = input("Enter a String: ")
count = 0
ch = input("Enter the character to count: ")
x = int(input("Enter the location from where it should start counting: "))
for i in range(x-1,len(str)):
    if str[i] == ch:
        count = count + 1
print ("Count of "+ch+" in "+str+" is :",count)