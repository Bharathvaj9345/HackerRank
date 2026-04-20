a=input("enter temperature : ")
b=input("enter humidity : ")
if(a=="warm" or a=="cold" or b=="dry" or b=="humid"):
   if(a=="warm" and b=="dry"):
      print("you can play basketball.")
   elif(a=="warm" and b=="humid"):
      print("you can play tennis.")
   elif(a=="cold" and b=="dry"):
      print("you can play cricket.")
   elif(a=="cold" and b=="humid"):
      print("you can do swimming.")
   else:
      print("you can play other games.")
else:
   print("enter valid temperature and humidity.")
