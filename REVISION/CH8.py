# # CHAPTER 8 - FUNCTIONS & RECURSION
# # PRACTICE SET (LEVEL 1 → LEVEL 3)

# # Q1. Create a function to print "Hello, World!".

# def printfunc():
#     print("hello world")

# printfunc()

# # Q2. Create a function to print your name.

# def name():
#     print("anurag kashyap")

# name()

# # Q3. Create a function that prints numbers from 1 to 10.

# def printnum():
#     for i in range(1,11):
#         print(i)
    
# printnum()

# # Q4. Create a function that takes your name as an argument and prints "Hello <name>".

# def greet(name):
#     print("good morning"+ name)

# greet("anurag")

# # Q5. Create a function that takes two numbers and prints their sum.

# def sum(a,b):
#     result = a + b
#     print(result)

# sum(2,3)

# # Q6. Create a function that takes a number and prints its square.

# def square(a):
#     result = a*a
#     print(result)

# square(45)

# # Q7. Create a function that takes a number and prints whether it is even or odd.

# def evenodd(a):
#     if a % 2 == 0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")

# evenodd(20)

# # Q8. Create a function that returns the sum of two numbers.

# def add(a, b):
#     return a + b

# add(7,7)
# print(add(7,7))

# # Q9. Create a function that returns the square of a number.

# def square(a):
#     return a*a

# print(square(4))

# # Q10. Create a function that returns the cube of a number.
# def cube(a):
#     return a*a*a

# print(cube(9))

# # Q11. Create a function that returns the largest of two numbers.

# def largest(a,b):
#     if a < b :
#         return f"{b} is largest"
#     else:
#         return f"{a} is largest"
# print(largest(987,562511))

# # Q12. Create a function that returns the smallest of two numbers.

# def smallest(a,b):
#     if a < b :
#         return f"{a} is smallest"
#     else:

#         return f"{b} is smallest"
# print(smallest(67,9))

# # Q13. Create a function that returns the largest of three numbers.

# def largest(a,b,c):
#     if a > b and a > c :
#         return f"{a} is largest"
#     elif b > a and b > c :
#        return f"{b} is largest"
#     elif c > a and c > b:
#         return f"{c} is largest"
# print(largest(23,25,26))

# Q14. Create a function that returns the factorial of a number.

def factorial(a):
    int = 1
    for i in range(1, a + 1):
        int = int * i
    print(f"Factorial = {int}")

factorial(22)

# Q15. Create a function that counts the vowels in a string.



# Q16. Create a function that counts the consonants in a string.

# Q17. Create a function that reverses a string.

# Q18. Create a function that checks whether a string is a palindrome.

# Q19. Create a function that returns the length of a list.

# Q20. Create a function that returns the largest element in a list.

# Q21. Create a function that returns the smallest element in a list.

# Q22. Create a function that returns the sum of all elements in a list.

# Q23. Create a function that counts how many times an element appears in a list.

# Q24. Create a function that returns the second largest element in a list.

# Q25. Create a function that returns the second smallest element in a list.

# Q26. Create a function that returns the most frequent element in a list.

# Q27. Create a function that returns the least frequent element in a list.

# Q28. Create a function that returns all elements occurring exactly once.

# Q29. Create a function that returns a dictionary of squares from 1 to n.

# Q30. Create a function that counts the frequency of each word in a sentence.

# ============================
# RECURSION
# ============================

# Q31. Write a recursive function to print numbers from 1 to n.

# Q32. Write a recursive function to print numbers from n to 1.

# Q33. Write a recursive function to find the sum of first n natural numbers.

# Q34. Write a recursive function to find the factorial of a number.

# Q35. Write a recursive function to calculate x raised to the power n.

# Q36. Write a recursive function to find the nth Fibonacci number.

# Q37. Write a recursive function to count digits in a number.

# Q38. Write a recursive function to reverse a string.

# Q39. Write a recursive function to check whether a string is a palindrome.

# Q40. Write a recursive function to find the sum of digits of a number.