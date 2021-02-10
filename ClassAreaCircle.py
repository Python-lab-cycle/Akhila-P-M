import math
class circle():
    def __init__(self,radius):
        self.radius1=radius
    def area(self):
        return(self.radius1*self.radius1*math.pi)
a=int(input("Enter radius:"))
obj=circle(a)
print("Area is:",obj.area())
