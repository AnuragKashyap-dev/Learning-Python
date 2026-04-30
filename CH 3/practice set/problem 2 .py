letter = '''
dear <|name|>,
you are selected !
<|date|>'''
a = letter.replace("<|name|>","anurag").replace("<|date|>","20 fevb 3039")
print(a)


# input version

letter = '''
dear <|name|>,
you are selected !
<|date|>'''
a = letter.replace("<|name|>",input("enter : ")).replace("<|date|>",input("enter : "))
print(a)



