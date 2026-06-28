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

# Q2.Find the second smallest number in a list.

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

# Q3.Find the largest even number in a list.

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

l = [2,3,4,7]
greatest = 0
average = (2+3+4+7)/4
for num in l:
    if num >average:
        greatest+=1
print(greatest) 

# Q6.Find the sum of all odd numbers in a list.

l = [1,3,4,7,9,2]
odd = 0
for num in l:
    if num%2 != 0 :
        odd += num
print(odd)

# Q7.Find the product of all elements in a list.

l = [2,4,6,8]
product = 1
for num in l:
    product = num*product
print(product)    

# Q8.Create a new list containing cubes of all numbers.

l = [2,3,4,5]
cube = [ ]
for num in l:
    if num not in cube:
        cube.append(num*num*num)
print(cube)        

# Q9.Remove duplicates from a list using loops.

l = [1,2,3,4,4,5]
l2 = []
for num in l :
    if num not in l2:
        l2.append(num)
print(l2)

# Q10.Find all duplicate elements in a list.
l = [1,2,3,3,4,5]
duplicate = []
for num in l:
    if l.count(num)>1 and num not in duplicate:
        duplicate.append(num)
    else:
        l2.append(num)
print(duplicate)

# 🔹 Section B: Strings
# Q11.Count vowels in a string.

str = "anurag"
vowels = "aeiouAEIOU"
count_vowel = 0
for words in str :
    if words in vowels :
        count_vowel += 1
print(count_vowel)

# Q12.Count consonants in a string.

str = "anurag"
vowels = "aeiouAEIOU"
count_consonent = 0
for words in str :
    if words not in vowels :
        count_consonent += 1
print(count_consonent)

# Q13.Count uppercase letters in a string.

str = "Anurag Kashyap"
uppercase_letters = 0
for letters in str:
    if letters.isupper():
        uppercase_letters += 1
print(uppercase_letters)


# Q14.Count lowercase letters in a string.

str = "Anurag Kashyap"
lowercase_letters = 0
for letters in str:
    if letters.islower():
        lowercase_letters += 1
print(lowercase_letters)

# Q15.Count digits in a string.

str = "anurag985"
digit_count = 0
for digit in str:
    if digit.isdigit():
        digit_count += 1
print(digit_count)

# Q16.Count spaces in a string.

str = "Anurag Kashyap 0 0 0"
space_count = 0
for digit in str:
    if digit.isspace():
        space_count += 1
print(space_count)

# Q17.Reverse a string using loops.

str = "anurag"
ulta_str = ""
for letter in str:
    ulta_str = letter + ulta_str
print(ulta_str)
        
# Q18.Find the longest word in a sentence.

sentence = "anurag is a begginner"
longest = ""
words = sentence.split()
for word in words :
    if len(word)>len(longest):
        longest = word
print(longest)

# Q19.Find the shortest word in a sentence.

sentence = "anurag is a begginner"
words = sentence.split()
smallest = words[0]
for word in words :
    if len(word)<len(smallest):
        smallest = word
print(smallest)

# Q20.Count frequency of each character in a string.

str = "heelooo"
frequency = {}
for words in str:
    if words in frequency:
        frequency[words]+= 1
    else:
        frequency[words] = 1
print(frequency)    

# 🔹 Section C: Loops + Conditions

# Q21.Print all numbers between 1 and 100 divisible by both 3 and 5.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

# Q22.Count how many numbers between 1 and 100 are divisible by 7.

number_divisibleby7=0
for num in range(1,101):
    if num%7==0:
        number_divisibleby7 += 1
print(number_divisibleby7)

# Q23.Find the sum of numbers from 1 to 100 divisible by 5.

sum = 0
for num in range(1,101):
    if num%5==0:
        sum = num+sum
print(sum)

# Q24.Print all prime numbers from 1 to 100.

for num in range(2, 101):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num)

# Q25.Check whether a given number is prime.

num = int(input("enter the number:- "))
factors = 0
for i in range(1,num+1):
    if num % i == 0:
        factors +=1
if factors == 2:
    print(f"yes, {num} is a prime number.")
else:
    print(f"no, {num} is not a prime number.")

# Q26.Count factors of a number.

num = int(input("enter a number:- "))
factors = 0
for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
print(f"{num} has {factors} factors")

# Q27.Find the greatest factor of a number other than itself.

num = int(input("enter a number:- "))
largest_factor = 0
for i in range(1,num+1):
      if num % i == 0 and i > largest_factor and i != num:
            largest_factor = i
print(largest_factor)

# # Q28.Find HCF of two numbers.

num1 = int(input("enter number1:- "))
num2 = int(input("enter number2:- "))
factor1 = [ ]
factor2 = [ ]
hcf = 0
for i in range(1,num1+1):
    if num1 % i == 0 :
        factor1.append(i)
for i in range(1,num2+1):
    if num2%i==0:
        factor2.append(i)
for nums in factor1:
    if nums in factor2 and nums>hcf:
        hcf = nums
print(hcf)

# Q29.Find LCM of two numbers.

a = 4
b = 6
largest = max(a, b)
while True:
    if largest % a == 0 and largest % b == 0:
        print("LCM =", largest)
        break
    largest += 1

# Q30.Check whether a number is a perfect number.

num = int(input("Enter number: "))
total = 0
for i in range(1, num):
    if num % i == 0:
        total += i
if total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# 🔹 Section D: Dictionaries & Loops

# Q31
# Count frequency of each element in a list.

l = [1, 2, 2, 3, 3, 3]
freq = {}
for num in l:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

# Q32.Count frequency of each word in a sentence.

sentence = "anurag is a coder"
words = sentence.split()
freq={}
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1
print(freq)

# Q33.Count frequency of each character in a string.

sentence = "anurag is anurag"
freq={}
for words in sentence:
  if words in freq:
    freq[words] += 1
  else:
    freq[words] = 1
print(freq)

# Q34.Find the student with highest marks from a dictionary.
 
dict = {"aryan":67,
        "abhi":34,
        "gian":88
}
items_dict = dict.values()
largest_marks = 0
for items in items_dict:
  if items > largest_marks:
    largest_marks = items
  
print(largest_marks)

# Q35.Find the student with lowest marks from a dictionary.

marks = {
    "Aman": 90,
    "Ravi": 85,
    "Anurag": 95,
    "Sita": 88,
    "Rahul": 80
}
lowest_marks = 100
lowest_student = ""
for student in marks:
    if marks[student] < lowest_marks:
        lowest_marks = marks[student]
print(lowest_marks)

# Q36.Create a dictionary of squares:
# Python
# 1 : 1
# 2 : 4
# 3 : 9
# ...
# 10 : 100

dict = {}
for i in range(1,11):
  dict[i]=i*i
print(dict)

# Q37.Invert a dictionary:
# Python
# {"a":1,"b":2}
# to
# Python
# {1:"a",2:"b"}

dict = {"a":1,"b":2}
dict2 = {}
for keys in dict :
    dict2[dict[keys]] = keys

print(dict2)

# Q38.Count occurrence of vowels using a dictionary.
str = "my name is anurag kashyap"
vowels = {
    "a":0,
    "e":0,
    "i":0, 
    "o":0,
    "u":0
}
for words in str:
    if words in vowels:
        vowels[words] += 1
print(vowels)

# 🔹 Section E: Pattern Recognition
# Q39.Find the largest odd number in a list.
# Q40.Find the smallest even number in a list.
# Q41.Count numbers greater than 50.
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