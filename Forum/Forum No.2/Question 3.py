import os

os.chdir('C:\\Users\\Intel\\Desktop\\BINUS\\Coding Stuff\\Algorithm & Python\\08-11-2021\\Book')
Base = open('98-0.txt',"r")
counted = open("Counted_Books.txt","x")
mybook = Base.read().split()

Wordcount = sum(len(words) for words in mybook)/ len(mybook)
counted.close()