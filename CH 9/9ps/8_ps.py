with open("log.txt","r") as f :
    content = f.read()
with open("log_copy.txt","w") as f :
    f.write(content)

