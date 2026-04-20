import math
a=int(input("enter 1st value : "))
b=int(input("enter 2nd value : "))
c=int(input("enter 3rd value : "))
x=(b*b)-(4*a*c)
y=x**0.5
if(y==0):
   u=(-1*b)/(2*a)
   print("the values are : ",u)
elif(x>0):
   k=((-1*b)+(y))/(2*a)
   n=((-1*b)-(y))/(2*a)
   print("the values are : ",k," & ",n)
else:
   z=(-1*x)
   m=(-1*b)/(2*a)
   p=(z**0.5)/(2*a)
   print("the value is : ",m,"+j",p)
   print("the value is : ",m,"-j",p)
