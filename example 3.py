#prog to calc the average score and average grade score
c=int(input("enter score fot c:" ))
java=int(input("enter score fot java: "))
python=int(input("enter score fot python: "))
score=((c+java+python)/3)
if(score>70 and score<100):
  print("A")
elif(score>60 and score<69):
  print("B")
elif(score>50 and score<59):
  print("C")
else:
    print("FAIL")