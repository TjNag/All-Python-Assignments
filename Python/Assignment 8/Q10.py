lt = input("Enter list elements : ").split()

maxm = sec = 0

if(int(lt[0])>int(lt[1])):
    maxm = int(lt[0])
    sec = int(lt[1])
else:
    maxm = int(lt[1])
    sec = int(lt[0])

for i in range (0, len(lt)):
    if int(lt[i]) > maxm:
        sec = maxm
        maxm = int(lt[i])
    elif int(lt[i]) > sec and int(lt[i]) < maxm:
        sec = int(lt[i])
print("Second largest element =", sec)