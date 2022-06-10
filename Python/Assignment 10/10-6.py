arr = [[0, 1, 0],
       [5, 0, 0],
       [0, 0, 3]]

dictionary = {}
 
# iterating through the matrix
for i in range(len(arr)):
    for j in range(len(arr[i])):
        dictionary[i, j] = arr[i][j]

print(dictionary)