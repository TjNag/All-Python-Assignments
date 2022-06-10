class Numbers:
    def __init__(self, n):
        self.num = n
    @classmethod
    def largest(cls, num):
        return max(num)

n = []
print("Enter 5 numbers:")
for i in range(5):
    x=int(input())
    n.append(x)
obj = Numbers(n)
print("Largest Number:",obj.largest(n))