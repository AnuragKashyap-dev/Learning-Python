# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


a1 = int(input("enter marks 1 : "))
a2 = int(input("enter marks 2 : "))
a3 = int(input("enter marks 3 : "))

total_percentage = (100*(a1 + a2 + a3 ))/300
if (total_percentage>=40 and a1>33 and a2>33 and a3>33):
    print("you are passed !!",total_percentage)

else:
    print("you are faILED , try again next year__",total_percentage)