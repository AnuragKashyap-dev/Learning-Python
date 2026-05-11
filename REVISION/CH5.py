# # Practice Set ( Dictionaries & Sets)
# # LEVEL 1

# # Q1.Create a dictionary with:
# # name
# # age
# # marks
# # Print all values.

# dict = {"name":"Anurag",
#         "age":"16",
#         "marks":"90"}
# print(dict.items())         

# # Q2. Access and print only the "marks" value.

# dict = {"name":"Anurag",
#         "age":"16",
#          "marks":"90"}

# print(dict.get("marks"))

# # Q3.Add a new key "city" to a dictionary.

# dict = {"name":"Anurag",
#         "age":"16",
#          "marks":"90"}
# dict["city"] = "delhi"
# print(dict)


# # Q4. Change value of an existing key.

# dict = {"name":"Anurag",
#         "age":"16",
#          "marks":"90"}

# dict.update({"name":"AVINASH"})
# print(dict.get("name"))

# # Q5. Print all keys of a dictionary.

# dict = {"name":"Anurag",
#         "age":"16",
#          "marks":"90"}

# print(dict.keys())

# # Q6.Print all values of a dictionary.

# dict = {"name":"Anurag",
#          "age":"16",
#          "marks":"90"}
# print(dict.values())

# # Q7.Create a set with duplicate values and observe output.
# s = {1,1,2,3,3,3,2,2,3,4,3,4,3,3,4,3,4,3}
# print(s)

# '''output: - {1,2,3,4}
# --> bcz sets can't contain duplicate values'''


# # Q8.Add an element to a set.
# s = {1,2,34,4,6,6}
# s.add("anurag")
# print(s)

# # Q9.Remove an element from a set.
# s = {1,2,3,4,5,6,7,8,}
# s.remove(1)
# print(s)


# LEVEL 2

# Q10.Count frequency of elements using dictionary.
# dict = {1,1,1,1,2,2,2,2,4,4,4}
# print()




# Q11.Check if a key exists in dictionary.
dict = {"name":"Anurag",
        "age":"16",
         "marks":"90",
         "marks":"25"}
if "marks" in dict:
        print("already exists")
else:
        print("new one")

# Q12.Merge two dictionaries.
dict1 = {"anurag"}
dict2 = {"kashyap"}
print(dict1.add(dict2))

# Q13

# Create a dictionary from two lists:

# keys = ["name", "age"]
# values = ["Anurag", 15]
# Q14

# Find common elements between two sets.

# Q15

# Find union of two sets.

# Q16

# Find difference between two sets.

# LEVEL 3
# Q17

# Take a sentence and count frequency of each word.

# Q18

# Store marks of 5 students in dictionary and print highest scorer.

# Q19

# Remove duplicate elements from a list using set.

# Q20

# Create a nested dictionary for 2 students:

# {
#  "Aman": {"Math": 90},
#  "Ravi": {"Math": 85}
# }

# Print specific marks.