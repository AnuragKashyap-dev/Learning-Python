class programmer :
   company = "microsoft"

   def __init__(self,name,salary,pin):
      self.name = name
      self.salary = salary
      self.pin = pin

p = programmer ("harry",1244,21343)
r  = programmer("rohan",678998,900)
print (r.name,r.salary,r.company,r.pin)