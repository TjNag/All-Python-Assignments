def Sphere(r):
    v=(4/3)*(22/7)*r**3
    p=2*(22/7)*r
    a=4*(22/7)*r*r
    print()
    print("Volume:", v)
    print("Perimeter:", p)
    print("Area:", a)

def Cuboid(l, b, h):
    v=l*b*h
    p=4*(l+b+h)
    a=2*(l*b + b*h + l*h)
    print()
    print("Volume:", v)
    print("Perimeter:", p)
    print("Area:", a)
    
def Cone(r, h):
    v= (1/3)*(22/7)*r*r*h
    p=2*(22/7)*r
    a=(22/7)*r*r
    print()
    print("Volume:", v)
    print("Perimeter:", p)
    print("Area:", a)
    
print("For Sphere:")
r=int(input("Enter radius: "))
Sphere(r)
print()
print("For Cuboid:")
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
h=int(input("Enter height: "))
Cuboid(l, b, h)
print()
print("For Cone:")
r=int(input("Enter radius: "))
h=int(input("Enter height: "))
Cone(r, h)