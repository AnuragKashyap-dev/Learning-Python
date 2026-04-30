import random
'''
1 = rock
-1 = paper
0 = scissors
'''
computer = random.choice([1,-1,0])
youstr =input("enter your choice: ")
youdict = {"r":1,"p":-1,"s":0}
reversedict = {1:"rock",-1:"paper",0:"scissors"}    
you = youdict[youstr]
print(f"computer chose {reversedict[computer]}")
print(f"you chose {reversedict[you]}")

if (computer == you):
    print("draw")

else:
    if (computer == -1 and you == 1):
      print("you lose")
    elif (computer == -1 and you == 0):
      print("you win")
    elif (computer == 1 and you == 0):    
      print("you lose")
    elif (computer == 1 and you == -1):    
      print("you win")
    elif (computer == 0 and you == 1):    
      print("you win")
    elif (computer == 0 and you == -1):    
      print("you lose")
    else:
      print("invalid input")


