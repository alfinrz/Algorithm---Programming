#Fraction
import math
from fractions import Fraction

X = eval(input("Please enter a numerator that is higher than 0:"))
Y = eval(input("Please enter a denominator that is higher than 0:"))
Z = math.gcd(X,Y)  
#After looking at others code, it seems like I'm the only one using eval for my input, wonder if it's ok or not

while True:
    if X > 0:
        break
    else:
        print("The numerator value cannot be computed")
        break

while True:
    if Y > 0:
        break
    else:
        print("The denominator value cannot be computed")
        break

Z = math.gcd(X,Y)    
print("the greatest common divisor is",Z)

#Found out/ remembered that anything you put in print, will be outputed as a string

if X<Y:     #This "if" statement is dedicated to determining wheter the number that was inserted, is a proper fraction or not
    print(X,"/",Y, "is a proper fraction")
    if Z>1:
        print(X//Z,"/",Y//Z, "The proper function has been reduced")
        print("This fraction have been reduced")
    else:
        print("This fraction cannot be reduced any further")
elif X>Y:   #This "elif" statement is for improper statement and also includes code that will make whole number and mixed fraction
    print(X,"/",Y, "is an improper fraction")
    X1=X//Z
    Y1=Y//Z
    #decided to seperate these "if" statement since there are multiple numbers that can conflict
    if Z>1 and Y1==1:   #The code if the improper fraction can be turned into a whole number providing the denominator is more than 1
        print(X1,"/",Y1, "This improper fraction have been reduced")
        if Y1==1:                                           
            print(X1//Y1, "This is a whole number")
    elif Z>1:   #To turn improper fraction into mixed fraction
        print(X1,"/",Y1, "This improper fraction have been reduced")
        Q = X1//Y1
        Q1 = X1%Y1 
        print("The mixed number is", Q,"and",Q1,"/",Y)
    elif Z==1 and Y1==1:    #for Numerator that are prime numbers while having 1 as their denominator
        print(X1//Y1, "This is a whole number")
    else:   #For mixed fraction where the improper fraction have a prime number as their denominator
        print("This fraction cannot be reduced any further")
        Q = X1//Y1
        Q1 = X1%Y1 
        print("The mixed number is", Q,"and",Q1,"/",Y)





    

