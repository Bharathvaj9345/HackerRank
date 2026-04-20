p=int(input("enter p value : "))
n=int(input("enter n value : "))
r=int(input("enter r value in percent : "))
N=int(input("enter N value : "))
x=(p*n*r)/100
print("the SI is : ",x)
c=(N*n)
z=p*(1+((r/100)/n))**c
#k=z**c
print("the entire CI is : ",z)
m=z-p
print("the CI alone is : ",m)
