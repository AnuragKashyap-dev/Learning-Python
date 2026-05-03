# LEVEL 1 (Basic control)
# Q1.Take a string and print:
# first character
# last character

str = "python"
print(str[0])
print(str[-1])
# Q2.Take a string and print:
# first 4 characters
# last 4 characters

str = "zebronics"
print(str[0:4])
print(str[5:])

# Q3.Given:
# s = "python"
# Print:
# pyt
# hon

s = "python"
print(s[0:3])
print(s[3:])

# Q4.Reverse a string using slicing.

str = "anurag"
print(str[::-1])    #bcz '::-1' this says that print from last to first bcz the skip value is -1

# Q5.Print this exactly:
# Hello
# World
# (using escape sequence)

print("hello\nworld")

# Q6.Convert a string to:
# uppercase
# lowercase

str  = "hemoglobin"
print(str.capitalize())
print(str.lower())
print(str)

# Q7.Count total characters in a string.

str = "royal"
print(len(str))

#LEVEL 2 (Concept building)

#Q8.Take a string and print every second character.

str = "royalchallengersbangalore"
print(str[0::2])

