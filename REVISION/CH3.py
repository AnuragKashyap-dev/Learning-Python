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

# #LEVEL 2 (Concept building)

# #Q8.Take a string and print every second character.

str = "royalchallengersbangalore"
print(str[0::2])

# Q9.Take a string and print characters from index 2 to 8 with step 2.

str = "horsecart"
print(str[2:8:2])


# Q10.=Given:
# s = "programming"
# Print:
# rga
# min

s = "programming"
print(s[1:6:2])
print(s[7:10])





# Q11.Check if a string starts with "A" and ends with "z".
stt = "Anurag"
print(stt.startswith("A"))
print(stt.endswith("z"))


# Q12.Replace all spaces in a string with _.
spaces = "   a   n   u   r  a   g  "
print(spaces.replace(" ","_"))


# Q13.Count how many times a character appears in a string.
str = "r o y a l"
print(str.count("r o y a l"))



# Q14.Print:
# He said "Python is easy"
# (using escape sequence)

str = "he said \'python is easy\'"
print(str)

# LEVEL 3 

# Q15.Take a string and:
# print even index characters
# print odd index characters

string = "geforcertx"
print(string[::2])  #even
print(string[::3])  #odd

# Q16.Given:
# s = "abcdefg"
# Print:
# aceg
# gfedcba

s = "abcdefg"
print(s[::2])
print(s[::-1])

# Q17. Take a string and remove first and last character using slicing.

str = "programming"
print(str[1:10])

# Q18.Check if a string is palindrome using slicing.

str = "level"
palindrome1 = str[::-1]
if str == palindrome1 :
    print("yes , this word is palindrome")



# Q19.Print this exactly:
# Name: Anurag
# Age: 15 (using escape sequences in one print)

print("Name : Anurag \n Age : 15")




