lt = [1, 2, 3 , 4, 5]

print("Before swapping first and last element = ", lt)

temp = lt[len(lt)-1]
lt[len(lt)-1] = lt[0]
lt[0] = temp

print("After swapping first and last element = ", lt)
