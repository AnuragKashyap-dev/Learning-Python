# 1. Print numbers from 1 to 10 using both for and while loop.
'''
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

# 7. Check whether a number is palindrome.

# 8. Check whether a number is prime.

# 9. Print Fibonacci series up to n terms.

# 10. Find sum of digits of a number.

# 11. Count vowels in a string using loop.

# 12. Reverse a string using loop.

# 13. Find largest element in a list using loop.

# 14. Remove duplicates from a list manually.

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

'''
# 18. Create menu-driven calculator using loop.

# 19. Keep taking input until user enters 0.
number = 0
num = int(input("Enter Number:- "))
while(num != number):
    print("try again")
    num = int(input("Enter Number:- "))
print("succesfull")

# 20. Guess the number game using loop.