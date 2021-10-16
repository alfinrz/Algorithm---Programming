E1 = eval( input("Enter lenght of T1:"))
E2 = eval( input("Enter lenght of T2:"))
E3 = eval( input("Enter lenght of T3:"))

if E1+E2>E3 and E2+E3>E1 and E3+E1>E2:
    print("The Perimeter is", round(E1+E2+E3,1))

else:
    print("perimeter is Invalid")

#I remember getting this task in an earlier class and recode it in a more efficient manner