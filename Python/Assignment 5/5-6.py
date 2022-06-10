def Consonant (str):
    s=''
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            continue
        else:
            s=s+i
    print("New String =",s)

str=input("Enter a String: ")
Consonant(str)