class bank():
    def __init__(self,acnt,name,types,amount):
        self.ac=acnt
        self.nm=name
        self.typ=types
        self.amnt=amount
    def prntdtls(self):
        print("Account Holder Name:",self.nm)
        print("Account Number:",self.ac)
        print("Account Type:",self.typ)
        print("Amount:",self.amnt)
    def withdrw(self,w1):
        return(self.amnt-w1)
n=input("Enter Name:")
t=input("Enter type:")
num=int(input("Enter Account Number:"))
am=int(input("Enter Ammount:"))
obj=bank(num,n,t,am)
print("Account Details")
obj.prntdtls()
w=int(input("Enter ammount to withdraw:"))
print("Balance Amount:",obj.withdrw(w))
