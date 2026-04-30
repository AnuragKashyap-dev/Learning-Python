# Write a program to find whether a given number is prime or not.

n = int(input("enter a number"))

for i in range(2,n):
    if (n%i) == 0:
        print("this is not a prime number!!!")
        break

else:
    print("yahh !! this is a prime number.")        
    


