#largest number between three numbers
print("enter the three numbers :")
num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))  
num3=int(input("enter the third number :"))
if(num1>num2 and num1>num3):
  print("num1 is the largest number")
elif(num2>num1 and num2>num3): 
  print("num2 is the largest number")
if(num3>num2 and num3>num1):  
  print("num3 is the largest number")
else:
  print("all numbers are the same")  
