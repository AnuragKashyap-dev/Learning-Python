num = 9
a = int(input("enter a number:- "))
while num != a:
  if num<a:
      print("smaller")
  elif num>a:
      print("larger")
  elif num == a:
      print("you caught that!!")
  a = int(input("enter a number:- "))