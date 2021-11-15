import os

os.chdir('C:\\Users\\Intel\\Desktop\\BINUS\\Coding Stuff\\Algorithm & Python\\08-11-2021\\Book')
base = open('98-0.txt',"r") #the text that was used, had most of the special characters remove due to the windows 10 issue we found on 
numbered = open("Numbered_Books.txt","x")

mybook = base.read().split("\n") #using split here in order to split each individual line from each other in order to allow the number at the start of every line
counter = 1  #the number where the code will start counting from
for mybook in mybook:
    numbered.write(str(counter)+"."+mybook+"\n") #the str is to tell that the numbers are strings
    #while \n is used to tell the computer to go to a new line after writing the previous code
    counter +=1
