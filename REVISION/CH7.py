# 1. Print numbers from 1 to 10 using both for and while loop.

for i in range(1,11):
  print(i)

i = 1
while i <= 10:
  print(i)
  i+=1

# 2. Print all even numbers between 1 and 50.

for i in range(1,51):
  if i%2==0:
    print(i)

# 3. Find sum of first n natural numbers.

n = int(input("Enter a number: "))
sum = 0

for i in range(1,n + 1):
    sum = sum + i

print(f"Sum = {sum}")

# 4. Print multiplication table of a number.

num = 8
for i in range(1,11):
  print(f"{num} X {i} = {i*num}")

"or"

num = int(input("enter a number:- "))
for i in range(1,11):
  print(f"{num} X {i} = {i*num}")

# 5. Find factorial of a number.

num = int(input("Enter a number: "))

int = 1

for i in range(1, num + 1):
    int = int * i

print(f"Factorial = {int}")

# 6. Reverse a number.

num = input("enter the number:- ")
reverse = ""
for digit in num:
    reverse = digit + reverse
print(reverse)    

# 7. Check whether a number is palindrome.

num = input("enter the number:- ")
palindrome = ""
for digit in num:
    palindrome = digit + palindrome
if num == palindrome:
   print("yes the number is palindrome")
else:
   print("no the number is not palindrome")

# 8. Check whether a number is prime.

num = int(input("enter the number:- "))

for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")

# 9. Print Fibonacci series up to n terms.

# 10. Find sum of digits of a number.

number = 122
str_number = str(number)
digit_sum = 0
for digits in str_number:
    digit_sum += int(digits)
print(digit_sum)

"use abs to remove sign if number contains negative sign"
# 11. Count vowels in a string using loop.

str = "anurag"
str2 = "aeiouAEIOU"
vowel = 0
for letter in str:
    if letter in str2:
        vowel +=1
print(vowel)     

# 12. Reverse a string using loop.

string = input("enter the number:- ")
reverse = ""
for words in string:
    reverse = words + reverse
print(reverse)

# 13. Find largest element in a list using loop.

list = [12,45,18,56]
largest = list[0]
for items in list:
    if items>largest:
        largest = items
print(f"{largest} is largest.")

# 14. Remove duplicates from a list manually.

l = [12,34,12,54,65]
l2 = []
for items in l:
    if items not in l2:
        l2.append(items)
print(l2)

# 15. Print pattern:
# *
# **
# ***
# ****

for i in range(1,5):
  print("*"*i)

# 16. Print pattern:
# ****
# ***
# **
# *

for i in range(4,0,-1):
  print("*"*i)

# 17. Create login system with 3 attempts.

print("---- LOGIN ----")
user = "anurag"
password = 122345
max_attempts = 3
attempts = 0

while(attempts<max_attempts):
    username = input("Enter Username:- ")
    psw = int(input("Enter Password:- "))

    if username == user and psw == password:
        print("Login Successfull")
    else:
        attempts +=1
        print("Invalid Pair !!!")
if attempts == max_attempts:
    print("too many attempts , access denied")

# 18. Create menu-driven calculator using loop.

choice = 0
while(choice != 5):
    print("1.add")
    print("2.substract")
    print("3.divide")
    print("4.multiply")
    print("5.exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        a = int(input("enter 1st number :- "))
        b = int(input("enter 2nd number :- "))
        print(f"the sum is {a+b}")
    elif choice == 2:
        a = int(input("enter 1st number :- "))
        b = int(input("enter 2nd number :- "))
        if b==0:
            print("cannot divide by zero!!")
        else:
            print(f"the difference is {a-b}")
    elif choice == 3:
        a = int(input("enter 1st number :- "))
        b= int(input("enter 2nd number :- "))
        print(f"the division is {a/b}")

    elif choice == 4:
        a = int(input("enter 1st number :- "))
        b = int(input("enter 2nd number :- "))
        print(f"the product is {a*b}")
    elif choice == 5:
        print("calculator exited")
    else:
        print("invalid choice!")

# 19. Keep taking input until user enters 0.
number = 0
num = int(input("Enter Number:- "))
while(num != number):
    print("try again")
    num = int(input("Enter Number:- "))
print("succesfull")

# 20. Guess the number game using loop.
number = 220
num = int(input("guess the number:- "))
while(num != number):
   print("try again!")
   num = int(input("guess the number:- "))
print("you guessed it RIGHT")