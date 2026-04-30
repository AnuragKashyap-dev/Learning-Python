#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
#to detect these spams.
s1 = "Make a lot of money" 
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"


user = input("enter comment:  ")
if (s1 in user or s2 in user or s3 in user or s4 in user ):
    print("spam detected !!!!!!!!!!!!!!!!!!!!!!!!!!! ")

else:
    print(" no spam detected ")    