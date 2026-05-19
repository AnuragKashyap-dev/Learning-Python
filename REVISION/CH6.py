# 🔥 Conditional Expressions — Ultimate Revision Practice Set
# This set is arranged from:
# basics
# logic building
# tricky conditions
# exam-style thinking
# Only chapter-related questions included.



# 🔹 LEVEL 1 — Absolute Basics

# Q1.Check whether a number is positive.

number = int(input("enter a number:- "))
if (number>0) :
    print(f"{number} is positive.")
else:
    print(f"{number} is negative !!")

# Q2.Check whether a number is negative.

number = int(input("enter a number:- "))
if (number<0) :
    print(f"{number} is negative !!")
else:
    print(f"{number} is positive.")

# Q3.Check whether a number is zero.

number = int(input("enter a number:- "))
if (number==0) :
    print(f"this '{number}' is zero")
else:
    print(f"this '{number}' is not zero.")

# Q4.Check whether a number is even or odd.

number = int(input("enter a number:- "))
if (number%2 == 0) :
    print(f"this '{number}' is even.")
else:
    print(f"this '{number}' is odd.")

# Q5.Check whether a number is divisible by 5.

number = int(input("enter a number:- "))
if (number%5 == 0) :
    print(f"this '{number}' is divisible by 5.")
else:
    print(f"this '{number}' is not divisible by 5.")


# Q6.Check whether a number is divisible by both 3 and 5.

number = int(input("enter a number:- "))
if (number%3== 0 and number%5== 0) :
    print(f"this '{number}' is divisible by 3 and 5.")
else:
    print(f"this '{number}' is not divisible by 3 and 5.")

# Q7.Check whether a person is eligible to vote (18+).

age = int(input("enter your age:- "))
if (age >= 18) :
    print("you are eligible to vote")
else:
    print(f"you are not eligible to vote come back after {18 - age} years")

# Q8.Find greater between two numbers.

number1 = int(input("enter the number1 :- "))
number2 = int(input("enter the number2 :- "))
if (number1 > number2):
    print("number 1 is greater")

elif(number1 == 0 or number2 ==0):
    print("number is equal to zero")    

elif(number2 == number1):
    print("both are same")

else:
    print("number2 is greater")

# Q9.Find smaller between two numbers.

number1 = int(input("enter the number1 :- "))
number2 = int(input("enter the number2 :- "))
if (number1 > number2):
    print(f"number {number1} is smaller")  
elif(number2 > number1):
    print(f"number {number2} is smallest")



# Q10.Check whether a character is vowel or consonant.

vowel = ("a,e,i,o,u")
letter = input("enter the letter:- ")
for letters in vowel:
    if letter in letters:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is consonent")    


# 🔹 LEVEL 2 — Core Logic Building
# Q11.Find greatest among 3 numbers.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a > b and a > c:
    print(f"{a} is greatest")

elif b > a and b > c:
    print(f"{b} is greatest")

else:
    print(f"{c} is greatest")

# Q12.Find smallest among 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print(f"{a} is smallest")

elif b < a and b < c:
    print(f"{b} is smallest")

else:
    print(f"{c} is smallest")

# Q13.Take marks and print:
# Pass (>=33)
# Fail

marks = int(input("enter your marks:- "))
if (marks >=33):
  print("you are passed....")
else:
  print("sorry , but you are failed!!!")

# Q14.Print grade:
# A (90+)
# B (75+)
# C (50+)
# Fail

marks = int(input("enter your marks:- "))

if (marks >=90):
  print(f"you got an 'A' ")
elif(marks>=75):
  print(f"you got an 'B' ")
elif(marks>=50):
  print(f"you got an 'C' ")
else:
  print("sorry , but you are failed!!!")

# Q15.Check whether year is leap year.

year = int(input("enter the year:- "))
if (year%4) == 0:
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

# Q16.Check whether character is:
# uppercase
# lowercase

word = input("Enter a word: ")

if word.isupper():
    print("The word is in uppercase")

elif word.islower():
    print("The word is in lowercase")

else:
    print("The word is mixed case")

# Q17.Check whether number is:
# positive
# negative
# zero
# (using if-elif-else)

number = int(input("enter the number:-"))
if (number>0):
  print(f"{number}  is positive ")
elif (number<0):
  print(f"{number}  is negative ")
else:
  print("number is equal to 0 ")

# Q18.Create a simple calculator:
# +
# -
# *
# /

print("====Calculator======")
print("operations = + , - , / , * ")
number1 = int(input("enter the number:- "))
operation = input("operation:- ")
number2 = int(input("enter another number:- "))
if operation == "/":
  print(f"{number1}/{number2} = {number1/number2}")
  
elif operation == "*":
  print(f"{number1}*{number2} = {number1*number2}")
  
elif operation == "+":
  print(f"{number1}+{number2} = {number1+number2}")
  
elif operation == "-":
  print(f"{number1}-{number2} = {number1-number2}")
else:
  print("invalid operation")

# Q19.Check whether a number lies between 1 and 100.

number = int(input("enter the number:- "))
if (number > 1) and (number < 100):
  print("yess,number is between 1 and 100")
else:
  print("noo,number is not in between 1 and 100")

# Q20.Check whether number is multiple of:
# 2
# 3
# both
# none

number = int(input("enter the number:- "))
if (number%3 == 0)and(number%2==0):
  print(f"{number} is divisible by both 2 and 3")
elif number%2 == 0:
  print(f"{number} is divisible by 2")
elif number%3 ==0:
  print(f"{number} is divisible by 3")
elif (number%3 == 0)and(number%2==0):
  print(f"{number} is divisible by both 2 nd 3")
else:
  print("none")

# 🔹 LEVEL 3 — Real Thinking Questions

# Q21.Find greatest among 4 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and a > c and a > d:
    print(f"{a} is greatest")

elif b > a and b > c and b > d:
    print(f"{b} is greatest")

elif c > a and c > b and c > d:
    print(f"{c} is greatest")

else:
    print(f"{d} is greatest")

# Q22.Check whether triangle is valid.
# (Hint: sum of two sides > third side)

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")

else:
    print("Invalid Triangle")

# Q23. Check whether a character is alphabet, digit, or special character.

word = input("Enter a character: ")

if word.isalpha():
    print("Alphabet")

elif word.isdigit():
    print("Digit")

else:
    print("Special Character")

# Q24. Create login system:
# correct username
# correct password

correctusername = "admin"
correctpassword = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correctusername and password == correctpassword:
    print("Login Successful")

else:
    print("Invalid Username or Password")

# Q25.ATM withdrawal system:
# sufficient balance
# valid amount

balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")

elif amount > balance:
    print("Insufficient balance")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
  
# Q26.Electricity bill calculator:
# different bill rates using conditions

units = int(input("Enter units:- "))

if units<=100:
  print(f"Electricity bill = {units*5}")

elif units<=200:
  print(f"Electricity bill = {(100*5)+((units-100)*10)}")

else:
  print(f"Electricity bill = {(100*5)+(100*10)+((units-200)*15)}")

# Q27.Check whether number is palindrome.

num = input("Enter the number:- ")
if num == num[::-1]:
  print("Number is palindrome")
else:
  print("No the number is not palindrome")

# Q28.Check whether a student passed in:
# all subjects
# or failed in one subject

"Let passing marks be 37"
marksgot1 = int(input("enter your marks in science:- "))
marksgot2 = int(input("enter your marks in english:- "))
marksgot3 = int(input("enter your marks in maths:- "))
marksgot4 = int(input("enter your marks in sst:- "))

if marksgot1 >= 37 and marksgot2 >= 37 and marksgot3 >= 37 and marksgot4 >= 37:
  print("you are passed")
elif marksgot1 >100 and marksgot2 > 100 and marksgot3 >100 and marksgot4 >100:
  print("marks can't exceed 100")
else:
  print("you are failed")

# Q29.Menu-driven program:
# 1. Add
# 2. Subtract
# 3. Exit

print("--Choose--")
print("1.Add")
print("2.Subtract")
print("3.Exit")

choice = int(input("Enter your Choice:- "))
if choice == 1:
  print("Addition")
  a = int(input("Enter 1st number"))
  b = int(input("Enter 2nd number"))
  print(f"Sum is {a+b}")
  
elif choice == 2:
  print("Substraction")
  a = int(input("Enter 1st number"))
  b = int(input("Enter 2nd number"))
  print(f"Difference is {a-b}")
  
elif choice == 3:
  print("Program Exited")
  
else:
  print("Incorrect choice")

# Q30.Find second greatest among 3 numbers.

a = int(input("enter 1st number:- "))
b = int(input("enter 2nd number:- "))
c = int(input("enter 3rd number:- "))
 
if a>b and a<c or a>c and a<b:
  print(f"{a} is second greatest")
elif b>a and b<c or b<a and b>c:
  print(f"{b} is second greatest")
elif c>b and c<a or c<b and c>a:
  print(f"{c} is second greatest")
elif a == b == c :
  print("all are same")
else:
  print("something went wrong!!")