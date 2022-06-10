class Parent():
    def first(self):
        print('This is Parent Class')
        
class Child(Parent):
    def second(self):
        print('This is Child Class')
print("Single Inheritance -")
obj = Child()
obj.first()
obj.second()

class level1:
      def first(self):
            print ('This is Level 1')

class level2(level1):
      def second(self):
             print ('This is Level 2')

class level3(level2):
      def third(self):
            print ('This is Level 3')
print("\nMultilevel Inheritance -")
obj=level3()
obj.first()
obj.second()
obj.third()

class Base1:
      def func1(self):
            print("This is Base Class 1")
class Base2:
      def func2(self):
            print("This is Base Class 2")

class Childof2(Base1 , Base2):
      def func3(self):
            print("This is Child Class")
print("\nMultiple Inheritance -")
obj = Childof2()
obj.func1()
obj.func2()
obj.func3()

class ParentClass:
	def func1(self):
		print("This is Parent Class.")
class Child1(ParentClass):
	def func2(self):
		print("This is Child 1.")
class Child2(ParentClass):
	def func3(self):
		print("This is Child 2.")
print("\nHierarchical Inheritance -")
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
