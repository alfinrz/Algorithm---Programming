import os

os.chdir('C:\\Users\\Intel\\Desktop\\BINUS\\Coding Stuff\\Algorithm & Python\\08-11-2021\\Book')
file = open('98-0.txt',"r")

mybook = file.read().split()
exluded = ["i.e.", "Mr.", "Ms.", "Dr."]
addline = []
for x in mybook:
    if "?" and "!" not in mybook:
        addline+=(x + ".")
        if x in exluded:
            continue
        else:
            addline+=(x+"\n")
