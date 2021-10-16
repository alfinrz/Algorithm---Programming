#The code for this one is not perfect since if you input a number that is lower than -58 it will still answer it as a valid input
import math
while True:
    X1 = eval(input("enter temperature in the range of -58 degrees Fahrenheit and 41 degrees Fahrenheit:"))
    if -58>=X1>=41:
        print("please input a valid number for temperature")
        continue
    X2 = eval(input("enter wind speed higher than 2 MPH:"))
    if X2<2:
        print("please input a valid number for wind speed")
        continue
    else:
        Wind_chill = 35.74 + (0.6215*X1) - (35.75*X2**0.16) + (0.4275*X1*X2**0.16)
        print("The wind chill index is %.3f" % Wind_chill)
    break

