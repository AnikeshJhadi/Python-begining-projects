#menu driven program
a=int(input("Enter the first number="))
b=int(input("Enter the second number="))
print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nPress 5 for quotient\nPress 6 for remainder\nPress 7 for exponentiation")
i=int(input("ENTER:"))
if i==1:
    print("Answer="+str(a+b))
elif i==2:
    print("Answer="+str(a-b))
elif i==3:
    print("Answer="+str(a*b))
elif i==4:
    print("Answer="+str(a/b))
elif i==5:
    print("Answer="+str(a//b))
elif i==6:
    print("Answer="+str(a%b))
elif i==7:
    print("Answer="+str(a**b))
else:
    print("Not a valid choice:Please try again")
