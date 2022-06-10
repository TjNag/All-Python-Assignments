def Armstrong(n):
    n1=n
    c=0
    while(n1>0):
        n1=n1//10
        c=c+1
    n1=n
    s=0
    while(n1>0):
        dig=n1%10
        n1=n1//10
        s=s+(dig**c)
    if(s==n):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")