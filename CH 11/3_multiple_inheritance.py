class mummy:
    company = "itc hwello"
    def show (self):
        print(f"my name is {self.name} and my salary is {self.salary}")

class papa:
    language = "python"
    def showlanguage (self):
      print(f"my name is {self.name} and my salary is {self.salary}")

class beta (mummy,papa):
    def printlanguage(self):
      print(f"my name is {self.name} and my salary is {self.salary}")


a = beta()
print(a.company)
        

