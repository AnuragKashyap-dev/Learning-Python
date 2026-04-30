class employee :
    language = "python"
    salary = 12000000


    def __init__(self):
        print(" i am crreating the onjey ")



    def getinfo(self):
        print(f"the lang is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet ():
        print("good match")



anurag = employee()
anurag.language = "java"

print ( anurag.salary , anurag.language )

anurag.getinfo()
anurag.greet()
