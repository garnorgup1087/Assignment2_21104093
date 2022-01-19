side1=int(input("Enter length of first side:",))
side2=int(input("Enter length of second side:",))
side3=int(input("Enter length of third side:",))
if((side1<int(side2+side3))and(side2<int(side3+side1))and(side3<int(side1+side2))):
    print("Yes")
else:
    print("No")