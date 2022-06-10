class Account:
    money = 0.0
    def deposit(self, m):
        self.money += m
    def withdraw(self, m):
        self.money -= m
    def printdetails(self):
        print("Remaining balance =",self.money)

obj = Account()
while(True):
    print("Press 1 to deposit")
    print("Press 2 to withdraw")
    print("Press 3 to Exit")
    ch = int(input())
    if ch==1:
        m = float(input("Enter amount to deposit: "))
        obj.deposit(m)
        obj.printdetails()
    if ch==2:
        m = float(input("Enter amount to withdraw: "))
        obj.withdraw(m)
        obj.printdetails()
    if ch==3:
        exit(0)