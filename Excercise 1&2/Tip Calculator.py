
X1 = eval(input("enter value for subtotal:"))
X2 = eval(input("enter value for tip %:"))

X3 = (X1*(X2/100))
#starting to learn that calculating everything in the print command might not be the best of ideas

print("Subtotal: $%.2f" % X1)
print("Tip: $%.2f" % (X1*(X2/100)))
print("Total: $%.2f" %(X1+X3))