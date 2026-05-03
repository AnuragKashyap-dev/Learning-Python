# # Q1. Swap without third variable
# # Take two numbers as input and swap them
a = input("enter a number 'a' :-  ")
b = input("enter a number 'b' :- ")
print("numbers are swapped!!")
print (f"the number 'a' is {b}")
print (f"the number 'b' is {a}")


# Q2. Type checker
# Take input from user and print its data type.
#  (Hint: input() always gives string — so think.)

x = input("Enter something: ")

try:
    x = int(x)
    print("Integer")
except:
    try:
        x = float(x)
        print("Float")
    except:
        print("String")

# Q3. List input & sum
# Take 5 numbers from user, store in list, print sum.

a  = int(input("enter a number - "))
b  = int(input("enter another number - "))
c  = int(input("enter another number - "))
d  = int(input("enter another number - "))
e  = int(input("enter another number - "))

l = [ ]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
sum = (a+b+c+d+e)
print(f"sum of {l} is {sum}")

# Q4. Simple interest
# Take P, R, T and calculate SI.

p = int(input("enter the principal amount - "))
r = int(input("enter the rate of interest - "))
t = int(input("enter time period - "))
SI = ((p*r*t)/100)
print(f"the simple interest of your principal {p} at a rate of {r} in {t}years is {SI}")

# Q5.Boolean logic

# a = 10
# b = 20
# Print result of:
# a > b
# a == 10 and b == 20
# # not(a > b)
a = 10 
b = 20
print(a>b)
print(a==10 and b ==20)
print(not(a>b))
# Q4. String operations

# Take a name and:
# Print it in uppercase
# Print first 3 characters
# Print reversed string

name = "anurag"
print(f"capital-  {name.upper()}")
print(f"reversed-  {name[::-1]}")
print(f"first three letters-  {name[0:3]}")


# Q7. Tuple vs List test

# Create:
# a list and modify it
# a tuple and try modifying it
# -- Observe the error and explain WHY.

list = [ ]
list.append(90)
list.append(9099)
print(list)

tuple = ( )

 #we can't modify a tuple as tuples are immutable.

# Q8. Unique values
# Take a list and remove duplicates using set.

liist = ["aple","aple"]
liist = list(set(liist))
print(liist)

# #Q9. Dictionary builder
# # Take name and marks of 3 students and store in dictionary.

dict = { }
name  = input("enter name : ")
marks  = input("enter marks : ")
name2  = input("enter name : ")
marks2  = input("enter marks : ")
name3  = input("enter name : ")
marks3  = input("enter marks : ")
dict[name]= marks
dict[name2]= marks2
dict[name3]= marks3
print(dict)

# Q10. Type conversion trap
# x = "10"
# y = 5
# Add them properly and print result.

x = "10"
y = 5
x = int(x)
print(x+y)

# Q11. Mixed data type list
# Create a list:
# [10, "hello", 3.5, True]
# Print type of each element'''

list = [10, "hello", 3.5, True]
for item in list:
    print(f"the type of {item} is {type(item)}")

# Q13. String to list conversion
# Take a sentence and convert it into list of words.

str = "hello everyone how are you all doing?" 
split = str.split()
print(split)



















