# Loops Practice Set (Intermediate → Advanced)

# Section A: Lists

# Q1.Find the second largest number in a list.

l = [123,435,63423,6,2354]
largest = 0 
second = 0
for num in l:
    if num>largest:
        largest = num
    else:
        if num>second and num<largest:
            second = num
print(second)

# # Q2.Find the second smallest number in a list.

l = [12,11,234,543]
smallest = l[0]
second_smallest = l[0]
for num in l:
    if num>smallest:
        smallest = num
    else:
        if num>second_smallest and num<smallest:
            second_smallest = num
print(second_smallest)

# # Q3.Find the largest even number in a list.

l = [24,56,87,65,66]
largest = 0
for num in l :
    if num%2 == 0 and num>largest:
        largest = num
print(largest)

# Q4.Find the smallest odd number in a list.

l = [32,34,5,65]
smallest = l[0]
for num in l :
    if num%2 != 0 and num<smallest:
        smallest = num
print(smallest)

# Q5.Count how many elements are greater than the average of the list.

# Q6.Find the sum of all odd numbers in a list.

l = [1,3,4,7,9,2]
odd = 0
for num in l:
    if num%2 != 0 :
        odd += num
print(odd)

# Q7.Find the product of all elements in a list.

# Q8
# Create a new list containing cubes of all numbers.
# Q9
# Remove duplicates from a list using loops.
# Q10
# Find all duplicate elements in a list.
# 🔹 Section B: Strings
# Q11
# Count vowels in a string.
# Q12
# Count consonants in a string.
# Q13
# Count uppercase letters in a string.
# Q14
# Count lowercase letters in a string.
# Q15
# Count digits in a string.
# Q16
# Count spaces in a string.
# Q17
# Reverse a string using loops.
# Q18
# Find the longest word in a sentence.
# Q19
# Find the shortest word in a sentence.
# Q20
# Count frequency of each character in a string.
# 🔹 Section C: Loops + Conditions
# Q21
# Print all numbers between 1 and 100 divisible by both 3 and 5.
# Q22
# Count how many numbers between 1 and 100 are divisible by 7.
# Q23
# Find the sum of numbers from 1 to 100 divisible by 5.
# Q24
# Print all prime numbers from 1 to 100.
# Q25
# Check whether a given number is prime.
# Q26
# Count factors of a number.
# Q27
# Find the greatest factor of a number other than itself.
# Q28
# Find HCF of two numbers.
# Q29
# Find LCM of two numbers.
# Q30
# Check whether a number is a perfect number.
# 🔹 Section D: Dictionaries & Loops
# Q31
# Count frequency of each element in a list.
# Q32
# Count frequency of each word in a sentence.
# Q33
# Count frequency of each character in a string.
# Q34
# Find the student with highest marks from a dictionary.
# Q35
# Find the student with lowest marks from a dictionary.
# Q36
# Create a dictionary of squares:
# Python
# 1 : 1
# 2 : 4
# 3 : 9
# ...
# 10 : 100
# Q37
# Invert a dictionary:
# Python
# {"a":1,"b":2}
# to
# Python
# {1:"a",2:"b"}
# Q38
# Count occurrence of vowels using a dictionary.
# 🔹 Section E: Pattern Recognition
# Q39
# Find the largest odd number in a list.
# Q40
# Find the smallest even number in a list.
# Q41
# Count numbers greater than 50.
# Q42
# Count negative numbers in a list.
# Q43
# Find the sum of positive numbers only.
# Q44
# Find the average of list elements.
# Q45
# Count how many elements are equal to the maximum element.
# 🔹 Challenge Questions
# Q46
# Find the second largest distinct element.
# Q47
# Find the second smallest distinct element.
# Q48
# Find the most frequent element in a list.
# Q49
# Find the least frequent element in a list.
# Q50
# Find all elements that occur exactly once.