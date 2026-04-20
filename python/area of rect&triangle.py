import math
a=int(input("enter choice : "))
if(a==1):
   x=int(input("enter the length : "))
   y=int(input("enter the breath : "))
   if(x==0 or y==0):
      print("enter valid input.")
   else:
      z=(0.5*x*y)
      print("the area is : ",z)
elif(a==2):
   l=int(input("enter the side : "))
   m=int(input("enter the side : "))
   n=int(input("enter the side : "))
   if(l==0 or m==0 or n==0):
      print("enter valid input.")
   else:
      s=(l+m+n)/2
      b=((s)*(s-l)*(s-m)*(s-n))
      c=(b**0.5)
      print("the area is : ",c)
else:
   print("invalid!enter correct value")
