class employee:
    name = "anurag"
    company = "itc hwello"
    salary = 120000
    def show (self):
        print(f"my name is {self.name} and my salary is {self.salary}")


class programmer(employee):
     def show (self):
           print(f"my name is {self.name} and my salary is {self.salary}")


a = employee()
b = programmer()

print(b.name,b.salary)

class tuu(programmer):
    def show (self):
       print(f"my name is {self.name} and my salary is {self.salary}")

c = tuu()
print(c.name)
