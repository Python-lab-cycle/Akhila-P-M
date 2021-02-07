from AreaPerimeterFunctions import *
while[True]:
    print("\n*****Menu*****")
    print("\n1.Circle")
    print("\n2.cuboid")
    print("\n3.sphere")
    print("\n4.Quit")
    print("********************")
    choice=int(input("enter choice:"))
    if(choice==1):
        r1=int(input("enter radius:"))
        area=circlearea(r1)
        print("\nArea is:"+str(area))
        perimeter=circleperimeter(r1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==2):
        l1=int(input("enter length:"))
        w1=int(input("enter width:"))
        h1=int(input("enter heigth:"))
        area=cuboidarea(l1,w1,h1)
        print("\nArea is:" + str(area))
        perimeter=cuboidperimeter(l1,w1,h1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==3):
        r1=int(input("enter radius:"))
        area=spherearea(r1)
        print("\nArea is:" + str(area))
        perimeter=sphereperimeter(r1)
        print("\nPerimeter is:" + str(perimeter))
    elif(choice==4):
        quit(0)
    else:
        print("Give a valid choice")
