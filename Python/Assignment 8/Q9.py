lt = input("Enter list elements : ").split()

minm = int(lt[0])
maxm = int(lt[0])

for i in range (0, len(lt)):
    if int(lt[i])<minm:
        minm = int(lt[i])
    if int(lt[i])>maxm:
        maxm = int(lt[i])

print("Maximum element =", maxm)
print("Minimum element =", minm)