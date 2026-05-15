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






# Q17.Check whether number is:
# positive
# negative
# zero
# (using if-elif-else)










# Q18.Create a simple calculator:
# +
# -
# *
# /

# Q19.Check whether a number lies between 1 and 100.

# Q20.Check whether number is multiple of:
# 2
# 3
# both
# none

# 🔹 LEVEL 3 — Real Thinking Questions
# Q21

# Find greatest among 4 numbers.

# Q22

# Check whether triangle is valid.

# (Hint: sum of two sides > third side)

# Q23

# Check whether a character is alphabet, digit, or special character.

# Q24

# Create login system:

# correct username
# correct password
# Q25

# ATM withdrawal system:

# sufficient balance
# valid amount
# Q26

# Electricity bill calculator:

# different bill rates using conditions
# Q27

# Check whether number is palindrome.

# Q28

# Check whether a student passed in:

# all subjects
# or failed in one subject
# Q29

# Menu-driven program:

# 1. Add
# 2. Subtract
# 3. Exit
# Q30

# Find second greatest among 3 numbers.