# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.


l = ["Harry", "Soham", "Sachin", "Rahul"]

for names in l:
   if (names.startswith("S")):
      print(f"good morning {names}")
