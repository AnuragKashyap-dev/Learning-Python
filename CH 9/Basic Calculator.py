# calculator

print("    C A L C U L A T O R    ")


one = float(input("1 number: "))
calculate = (input("Enter expression: "))
two = float(input("2 number: "))
if "+" == calculate:
    print(f"the result is {one+two}")
    c = (f"{one}+{two}={one+two}")
elif "-" == calculate:
    print(f"the result is {one-two}")
    c = (f"{one}-{two}={one-two}")
elif "/" == calculate:
    print(f"the result is {one/two}")
    c = (f"{one}/{two}={one/two}")
elif "*" == calculate:
    print(f"the result is {one*two}")
    c = (f"{one}*{two}={one*two}")
else:
    print("invalid symbol!!")    

with open("history.txt","w") as f:
    f.write(c)






