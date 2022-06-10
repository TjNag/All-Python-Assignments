dictionary = {}

for i in range(1, 11):
    if i%2!=0:
        dictionary['{}'.format(i)] = i

print(dictionary)