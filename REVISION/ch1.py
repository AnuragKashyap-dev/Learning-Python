# Q1. Swap without third variable
# Take two numbers as input and swap them

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





















