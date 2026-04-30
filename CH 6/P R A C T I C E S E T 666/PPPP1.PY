#Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("enter a number: "))
a2 = int(input("enter a number: "))
a3 = int(input("enter a number: "))
a4 = int(input("enter a number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("this is greatest: ",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("this is greatest: ",a2)
if(a3>a2 and a3>a1 and a3>a4):
    print("this is greatest: ",a3)
if(a4>a2 and a4>a3 and a4>a1):
    print("this is greatest: ",a4)




