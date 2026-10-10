# FILE I/O — 30 PRACTICE QUESTIONS

# 1. Create data.txt and write "Hello Python" into it.

f = open("data.txt","w")
f.write("Hello Python")
f.close()

# 2. Open data.txt in read mode and print its complete content.

f = open('data.txt',"r")
text = f.read()
print(text)

# 3. Write your name, age, and city into a file, each on a new line.

with open("me.txt","w") as f:
    f.write("Anurag \n14 \nMotihari")

# 4. Read a file using read() and print the result.

with open("me.txt","r") as f :
    text = f.read()
print(text)

# 5. Read only the first 10 characters of a file using read().

with open("10.txt","r") as f:
    data = f.read(10)
    print(data)

# 6. Read the first line of a file using readline().

with open("10.txt","r") as f :
    data = f.readline()
    print(data)

# 7. Read all lines using readlines() and print the resulting list.

with open("10.txt","r") as f:
    data = f.readlines()
print(data)

# 8. Read a file line-by-line using a for loop.

with open("10.txt","r") as f:
    for line in f:
        print(line.strip())

# 9. Count the number of lines in a file.

count = 0
with open("Girl.txt","r") as file:
  for line in file:
    count += 1
print(count)

# 10. Count the number of words in a file.



# 11. Count the number of characters in a file.

# 12. Count how many times the word "Python" appears in a file.

# 13. Print only the lines that contain the word "Python".

# 14. Read a file and print each line with its line number.

# 15. Create a file containing numbers from 1 to 10, one number per line. Then read and print them.

# 16. Write "Hello" to a file, then use append mode to add "World" without deleting "Hello".

# 17. Take 5 names from the user and append them to a file.

# 18. Create a file using w mode, put some content in it, reopen it using w mode, and observe what happens.

# 19. Add a new sentence to an existing file without removing its previous content.

# 20. Write "Python is easy" to a file using the with open() statement.

# 21. Read a file using with open() and print its contents.

# 22. Read a file line-by-line using with open() and a loop.

# 23. Count the number of words in a file using with open().

# 24. Create a file containing several numbers. Read them and calculate their sum.

# 25. Read a file and find the longest word.

# 26. Read a file and count the number of vowels.

# 27. Read a file containing numbers and count how many are even and how many are odd.

# 28. Read a file and create another file containing only the lines that contain the word "Python".

# 29. Take a sentence from the user and append it to a file. Then read the complete file and display it.

# 30. Create a simple student record file where the user can repeatedly enter names and marks, save them using append mode, and finally read and display all records.