lt = input("Enter list elements : ").split()

element = input("Enter element to check if it exists in list : ")

i=0

for i in range (0, len(lt)):
    if lt[i]==element:
        break

if i<len(lt)-1:
    print("Element was found in list at index", i)
else:
    print("Element was not found in list")