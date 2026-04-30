with open("log.txt","r") as f :
    content = f.read()
word = "python"
if word in content:
    print("found!!!")
else:
    print("nothing is found!!!")    
