str=input("Enter a String: ")
s=''
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        continue
    else:
        s+=i
print("New String =",s)