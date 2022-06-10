lt = input("Enter list elements : ").split()

even = odd = 0

for i in range (0, len(lt)):
    if int(lt[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

print("No of even elements :", even)
print("No of odd elements :", odd)