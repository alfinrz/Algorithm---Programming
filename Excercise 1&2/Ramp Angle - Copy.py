#There is actually two different file for this
#This specific one is when my friend thought me how to create my own custom fuction
#The other one is when I did it without
import math
def calculate_angle(mass,force,gravity):
    d = math.degrees(math.asin(force / (mass * gravity)))  
    return d
m = eval(input("enter value for mass in kg:"))
f = eval(input("enter value for force in N:"))
g = 9.8

answer = calculate_angle(m,f,g)

print("The angle of the ramp is %.1f"% answer, "degrees")
