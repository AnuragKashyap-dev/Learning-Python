# Sum of all numbers in a list

l = [1,2,3,5]
total = 0
for num in l:
    total = num+total
print(total)    

# Count odd numbers in a list.

l = [1,2,3,5]
odd = 0 
for num in l :
    if num%2 != 0 :
        odd +=1
print(odd)    
    
# Find smallest number in a list

l = [2,3,4,5]
smallest = l[0]
for num in l :
    if num<smallest:
        smallest = num
print(smallest)

# Sum of even numbers only

l = [1,2,3,4,5,6]
even = 0
for num in l:
    if num%2 == 0 :
        even = num+even
print(even)

# Find largest odd number in a list

l = [1,2,3,5]
largest = 0
for num in l :
    if num%2 != 0 and num>largest:
        largest = num
print(largest)



