from calculatorFunctions import *
while[True]:
    num1=int(input("enter number1:"))
    num2=int(input("enter number2:"))
    print("\n*****Calculator Menu*****")
    print("\n1.Addition")
    print("\n2.subtraction")
    print("\n3.Multiplication")
    print("\n4.Division")
    print("\n5.Quit")
    print("********************")
    choice=int(input("enter choice:"))
    if(choice==1):
        result=addition(num1,num2)
        print("\nResult:"+str(result))
    elif(choice==2):
        result = subtraction(num1, num2)
        print("\nResult:" + str(result))
    elif(choice==3):
        result = multiplication(num1, num2)
        print("\nResult:" + str(result))
    elif(choice==4):
        result = division(num1, num2)
        print("\nResult:" + str(result))
    elif(choice==5):
        quit(0)
    else:
        print("Give a valid choice")
