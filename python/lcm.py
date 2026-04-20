a=int(input("enter a number : "))
b=int(input("enter a number : "))
temp1=a
temp2=b
while(b!=0):
   a,b=b,a%b
x=(temp1*temp2)/a
print("the LCM is : ",x)
