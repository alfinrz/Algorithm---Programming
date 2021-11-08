import os
from collections import Counter

os.chdir('C:\\Users\\Intel\\Desktop\\BINUS\\Coding Stuff\\Algorithm & Python\\08-11-2021\\Book')
file = open('98-0.txt',"r")

mybook = file.read()

count = Counter(mybook.lower().split())

for Hapax in count:
    if count[Hapax] == 1:
        print (Hapax)