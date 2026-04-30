def great(a,b,c):
    if (a>b ,a>c):
      return(a)
    elif (b>a,b>c):
      return(b) 
    elif (c>a,c>b):
       return(c)

a = 4
b = 5 
c = 1

print(great(a,b,c))