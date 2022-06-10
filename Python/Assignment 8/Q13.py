lt = input("Enter list elements : ").split()

print("Unsorted list :", lt)

for i in range (len(lt)-1, 0, -1):
    for j in range(i):
        if int(lt[j]) > int(lt[j+1]):
            temp = lt[j]
            lt[j] = lt[j+1]
            lt[j+1] = temp
print("Sorted list :", lt)