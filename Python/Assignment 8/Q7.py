lt = input("Enter list elements : ").split()

e = input("Enter element to check occurence : ")

found = 0

for i in range(0, len(lt)):
    if e == lt[i]:
        found += 1

print("Element", e, "was found", found, "times")