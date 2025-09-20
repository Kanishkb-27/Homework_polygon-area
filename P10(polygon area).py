from abc import ABC,abstractmethod
class polygon(ABC):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        pass
class triangle(polygon):
    def area(self):
        return 1/2*self.base*self.height
class rectangle(polygon):
    def area(self):
        return self.base*self.height
while (True):
    print("Which polygon's area do you want to calculate?")
    print("1. Triangle")
    print("2. Rectangle")
    choice=input()
    if choice not in ['1','2']:
        print("Please enter a valid option")
        continue
    else:
        choice=int(choice)
    if choice==1:
        b=int(input("Enter the measure of base of the triangle"))
        h=int(input("Enter the measure of height of the triangle"))
        obj=triangle(b,h)
        print("The area is",obj.area())
    elif choice==2:
        l=int(input("Enter the measure of the length of the rectangle"))
        b=int(input("Enter the measure of the breadth of the rectangle"))
        obj=rectangle(l,b)
        print("The area is",obj.area())
    else:
        print("Invalid option")