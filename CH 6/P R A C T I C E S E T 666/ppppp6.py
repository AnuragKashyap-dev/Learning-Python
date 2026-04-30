# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

number = int(input("enter your marks"))
if(number<=100 and number>=90):
    print("excellent")
elif(number<=90 and number>=80):
    print("a")
elif(number<=80 and number>=70):
    print("b")
elif(number<=70 and number>=60):
    print("c")
elif(number<=60 and number>=50):
    print("d")
elif(number<=50):
    print("f")



