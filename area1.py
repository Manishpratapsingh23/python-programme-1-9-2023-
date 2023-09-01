a=float(input("enter first side of triangle: "))
b=float(input("enter second side of triangle: "))
c=float(input("eneter third side 0f triangle: "))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("area of triangle: ",a)


