lt = input("Enter list elements : ").split()

add = 0

for i in range(0, len(lt)):
    add += int(lt[i])

print("Sum of all numbers in the list =", add)