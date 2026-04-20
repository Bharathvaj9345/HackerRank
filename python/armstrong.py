a=int(input("enter a number : "))
temp=int(a)
b=0
while(a!=0):
   c=int(a%10)
   b+=c**3
   a=a/10
if(b==temp):
   print("the number is an armstrong number.")
else:
   print("the number is not an armstrong number.")
