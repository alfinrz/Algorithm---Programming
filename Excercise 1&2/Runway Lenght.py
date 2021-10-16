#Same as the first code, rather simple

X1 = eval(input("enter value for velocity as m/s:"))
X2 = eval(input("enter value for acceleration m/s^2:"))

print("The minimum runway lenght needed for this airplane is %.4f" %(X1**2/(2*X2)),"meters")

#This is the point where I find out that being precise with what you want the code to do, is very important.