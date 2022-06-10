class Circle:
    PI = 22/7
    def __init__(self, r):
        self.rad=r
    def calc(self):
        self.area = self.PI * self.rad * self.rad
        self.circum = 2 * self.PI * self.rad
    def printdetails(self):
        print(f"Area: {self.area}\nCircumference: {self.circum}")

radius = float(input("Enter radius of circle: "))
obj = Circle(radius)
obj.calc()
obj.printdetails()