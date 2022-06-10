lt = input("Enter list elements : ").split()

neg = pos = 0

for i in range (0, len(lt)):
    if int(lt[i]) >= 0:
        pos += 1
    else:
        neg += 1

print("No of positive elements :", pos)
print("No of negative elements :", neg)