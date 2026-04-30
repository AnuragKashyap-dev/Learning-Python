f = open("poems.txt")
t = f.read()
f.close()
if "twinkle" in t:
    print("found")
else:
    print("noo")    