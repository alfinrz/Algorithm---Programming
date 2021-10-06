op = eval(input("Select number to a choose an operation (1. Addition, 2. Subtraction, 3. Multiplication, 4. Division:"))

X1 = eval(input("enter value No.1:"))
X2 = eval(input("enter value No.2:"))

if op==1:
    print(X1 + X2)
elif 1<op<=2:
    print(X1 - X2)
elif 2<op<=3:
    print(X1*X2)
elif 3<op<=4:
    print(X1 / X2)
else: 
    print("Value does not compute")

print("Thank you for using this calculator!")
