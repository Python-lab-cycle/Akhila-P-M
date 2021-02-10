class student:
    def __init__(self,dsmark,semark):
        self.mark1=dsmark
        self.mark2=semark
    def sum(self):
        return(self.mark1+self.mark2)
a=int(input("Enter mark obtained in DS:"))
b=int(input("Enter mark obtained in SE:"))
c=int(input("Enter RollNumber:"))
obj=student(a,b)
print("RollNumber is:",c)
print("Total mark is:",obj.sum())
