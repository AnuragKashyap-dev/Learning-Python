# Practice Set ( Dictionaries & Sets)
# LEVEL 1

# Q1.Create a dictionary with:
# name
# age
# marks
# Print all values.

dict = {"name":"Anurag",
        "age":"16",
        "marks":"90"}
print(dict.items())         

# Q2. Access and print only the "marks" value.

dict = {"name":"Anurag",
        "age":"16",
         "marks":"90"}

print(dict.get("marks"))

# Q3.Add a new key "city" to a dictionary.

dict = {"name":"Anurag",
        "age":"16",
         "marks":"90"}
dict["city"] = "delhi"
print(dict)


# Q4. Change value of an existing key.

dict = {"name":"Anurag",
        "age":"16",
         "marks":"90"}

dict.update({"name":"AVINASH"})
print(dict.get("name"))

# Q5. Print all keys of a dictionary.

dict = {"name":"Anurag",
        "age":"16",
         "marks":"90"}

print(dict.keys())

# Q6.Print all values of a dictionary.

dict = {"name":"Anurag",
         "age":"16",
         "marks":"90"}
print(dict.values())

# Q7.Create a set with duplicate values and observe output.
s = {1,1,2,3,3,3,2,2,3,4,3,4,3,3,4,3,4,3}
print(s)

'''output: - {1,2,3,4}  bcz sets can't contain duplicate values'''


# Q8.Add an element to a set.
s = {1,2,34,4,6,6}
s.add("anurag")
print(s)

# Q9.Remove an element from a set.
s = {1,2,3,4,5,6,7,8,}
s.remove(1)
print(s)


# LEVEL 2

# Q10.Count frequency of elements using dictionary.

l = [1, 2, 2, 3, 3, 3]

frequency = {}

for item in l:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
# Q11.Check if a key exists in dictionary.
dict = {"name":"Anurag",
        "age":"16",
         "marks":"90",
         "marks":"25"}
if "marks" in dict:
        print("already exists")
else:
        print("new one")

# # Q12.Merge two dictionaries.
# dict1 = {"anurag":"kashyap"}
# dict2 = {"kashyap":"anurag"}

dict = {"name":"Anurag"}
d2 = {"age":"15"}
dict.update(d2)

print(dict)

# Q13.Create a dictionary from two lists:
# keys = ["name", "age"]
# values = ["Anurag", 15]


# Q14.Find common elements between two sets.
s = {1,2,3}
s2 = {3,4,5}
print(s.intersection(s2))

# # Q15.Find union of two sets.
s = {1,2,3}
s2 = {3,4,5}
print(s.union(s2))


# # Q16.Find difference between two sets.
s = {1,2,3,4}
s2 = {2,5,6}
print(s.difference(s2))


# LEVEL 3
# Q17.Take a sentence and count frequency of each word.

line = "my name is anurag kashyap"
words = line.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)


# Q18.Store marks of 5 students in dictionary and print highest scorer.

marks ={"Aman": 90,
    "Ravi": 85,
    "Anurag": 95,
    "Sita": 88,
    "Rahul": 80}

highest = max(marks,key = marks.get)
print("highest scorer",highest)
print("highest marks",marks[highest])

# Q19.Remove duplicate elements from a list using set.

duplicate = (1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,5,5,5,5,5,5)
set1 = set(duplicate)
print(set1)

# Q20.Create a nested dictionary for 2 students:
# {
#  "Aman": {"Math": 90},
#  "Ravi": {"Math": 85}
# }
# Print specific marks.

marks =  {
  "Aman": {"Math": 90},
  "Ravi": {"Math": 85}
 }

print(marks["Aman"]["Math"])