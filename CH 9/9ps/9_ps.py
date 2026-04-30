with open("log.txt","r") as f :
    content1 = f.read()
with open("log_copy.txt","r") as f :
    content2 = f.read()
    
if content1 == content2:
    print("identical")
else:
    print("nope")        