#There is actually two different file for this
#This specific one is me using existing knowledge/ research
#The other one is when my friend thought me about custom function
import math
m = eval(input("enter value for mass in kg:"))
f = eval(input("enter value for force in N:"))
g = 9.8

sin_theta = f / (m * g)

a = math.asin(sin_theta)

d = math.degrees(a)

print("The angle of the ramp is %.1f"%d, "degrees")

#As said before, the module does help immensely when doing this type of programming.