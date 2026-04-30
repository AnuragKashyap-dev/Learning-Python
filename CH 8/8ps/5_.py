def count(n):
    if(n == 0):
        print("")
        return
    print("*"*n)
    count(n-1)



count(5)