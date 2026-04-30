class employee:
    company = "itc hwello"
    def show (self):
        print(f"my name is {self.name} and my salary is {self.salary}")

# class programmer :
#     company = "itc"  
#     def show (self):
#         print(f"my name is {self.name} and my salary is {self.salary}")

#     def showlanguage (self):
#         print(f"my name is {self.name} and my salary is {self.salary}")

class programmer(employee):
    company = ""
    def showlanguage (self):
      print(f"my name is {self.name} and my salary is {self.salary}")

a = employee
b = programmer
print(a.company , b.company)


        