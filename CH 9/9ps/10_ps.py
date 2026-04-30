with open("file.txt","r") as f :
    content = f.read()

if content != "":
    content = content.replace(content,"")
with open("file.txt","w") as f :
    f.write(content)
    
