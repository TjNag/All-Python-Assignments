'''
A               65
AB              65 66
ABC             65 66 67
ABCD            65 66 67 68
'''

for i in range(ord('A'),ord('E')):
    for j in range(ord('A'),i+1):
        print(chr(j), end='')
    print()


#i=1;i<=4;i++
#j=1;j<=i;j++