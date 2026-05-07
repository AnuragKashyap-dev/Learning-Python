# #Ch - 4                 Lists And Tuples
# #                        (PRACTICE SET)

# 🔹 LEVEL 1 (Basics you must not miss)

# Q1.Create a list of 5 integers and 
# print:
# first element
# last element
list = ["anurag",923,0.15,"herohonda"]
print(list[0])
print(list[3])

# Q2.Take a list and print its length.

lisst = ["anurag",788,0.1444,"herohonda","joker"]
print(len(lisst))

# Q3.Given:
# l = [10, 20, 30, 40]
# Print:
# first two elements
# last two elements

l = [10, 20, 30, 40]
print(l[0])
print(l[1])
print(l[2])
print(l[3])

# Q4.Reverse a list using slicing.

list = [10, 20, 30, 40]
print(list[::-1])

# Q5.Add an element at the end of a list.

list = [10, 20, 30, 40]
list.append(55)
print(list)

# Q6.Remove an element from a list.

list = [10, 20, 30, 40, 89, 90]
list.remove(89)
print(list)

# Q7. Create a tuple and print:
# first element
# last element

tuple = (1,4,566,885,33,54)
print(tuple[0])
print(tuple[5])

# Q8.Check length of a tuple.
tuple2 = (76,90,355,32,67,76,56)
print(len(tuple2))


# 🔹 LEVEL 2 (Concept building)


# Q9.Take a list and print all elements using indexing.

liist = ["orange",900,0.14,"anurag"]
print(liist[0])
print(liist[1])
print(liist[2])
print(liist[3])

# Q10.Find the maximum element in a list.

liist = [23,56,899]
print(max(liist))

# Q11.Count how many times an element appears in a list.

liist = [1,1,1,2,2,2,3,4,5,5,6,6,6]
count1  = (liist.count(1))
count2 = (liist.count(2))
count3 = (liist.count(3))
count4 = (liist.count(4))
count5 = (liist.count(5))
count6 = (liist.count(6))
print(f"1:- {count1}")
print(f"2:- {count2}")
print(f"3:- {count3}")
print(f"4:- {count4}")
print(f"5:- {count5}")
print(f"6:- {count6}")

# Q12.Convert a list into a tuple.

lisst = [1,34,5,67,33]
s = tuple(lisst)
print(type(s))

# # Q13.Convert a tuple into a list.

tuple = (1,34,5,67,33)
s = list(tuple)
print(type(s))

# Q14.Check if an element exists in a list.

list = [1,34,5,67,33,1]
print(1 in (list))

# Q15 .Given:
# l = [1, 2, 3, 4, 5]
# Print elements at even index positions.

l = [1, 2, 3, 4, 5]
print(l[1::2])













# 🔹 LEVEL 3 (Where real understanding shows)
# Q16

# Remove duplicates from a list (keep order).

# Q17

# Take a list and:

# create a new list with squares of elements
# Q18

# Swap first and last element of a list.

# Q19

# Given:

# t = (10, 20, 30)

# Try to change value and observe error.
# 👉 Explain why it happens.

# Q20

# Merge two lists into one.

# Q21

# Find the second largest element in a list.

# Q22

# Take a list and:

# separate even and odd numbers into two lists
# Q23

# Given:

# l = [1, 2, 3]

# Predict output:

# a = l
# a.append(4)
# print(l)
# Q24

# Create a tuple with mixed data types and print type of each element.