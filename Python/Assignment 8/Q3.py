lt = input("Enter list elements : ").split()
x, y = input("Enter indexes to swap elements : ").split()
print("Before swapping elements at index", x, "and", y, "list =", lt)

x = int(x)
y = int(y)

temp = lt[x]
lt[x] = lt[y]
lt[y] = temp

print("After swapping elements at index", x, "and", y, "list =", lt)