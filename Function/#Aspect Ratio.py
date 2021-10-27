#Aspect Ratio
import math


def calcNewHei():
    w = eval(input("Enter current width:"))
    h = eval(input("Enter current height:"))
    dw = eval(input("Enter desired width:"))
    gd = h/w
    x = gd * dw
    print("The corresponding height is:",x)

calcNewHei()