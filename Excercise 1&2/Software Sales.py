X = eval(input("enter quantity of desired packages to be purchased:"))

if X in range(10,19):
    print("Number of Packages purchased:",X)
    print("Discount Amount @ 10%%: $%.2f"%(X*99*10/100))
    print("Total amount: $%.2f" % (X*99*90/100))
if X in range(20,49):
    print("Number of Packages purchased:",X)
    print("Discount Amount @ 20%%: $%.2f" % (X*99*20/100))
    print("Total amount: $%.2f" % (X*99*80/100)) 
if X in range(50,99):
    print("Number of Packages purchased:",X)
    print("Discount Amount @ 30%%: $%.2f"%(X*99*30/100))
    print("Total amount: $%.2f" % (X*99*70/100))
if X>=100:
    print("Number of Packages purchased:",X)
    print("Discount Amount @ 40%%: $%.2f" % (X*99*40/100))
    print("Total amount: $%.2f" % (X*99*60/100)) 
if X<10:
    print("Number of Packages purchased:",X)
    print("Discount Amount @ 0%: $0.00")
    print("Total amount: $%.2f" % (X*99)) 
elif X<=0:
    print("Number must be more than 0")

#quite a reasonable code, but I would say could be a condensed.