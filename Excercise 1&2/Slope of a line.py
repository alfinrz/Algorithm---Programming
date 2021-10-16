# This is a rather simple code 

X1 = eval(input("enter value for y2:"))
X2 = eval(input("enter value for y1:"))
X3 = eval(input("Enter value for x2:"))
X4 = eval(input("Enter value for x1:"))
#After looking back at this code, not sure why I marked the variable like above

X5 = (X1-X2)/(X3-X4)
print("The slope for the line that connects two points", (X4, X2),"and",(X1,X3) ,"is %.5f" % X5)
#Knowning where to put the formating line was probably the trickiest since it has multiple string in the print command