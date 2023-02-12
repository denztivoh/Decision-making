#test

eng=int(input("enter marks for eng: "))
math=int(input("enter marks for math : "))
cre=int(input("enter marks for cre: "))
score=((eng+math+cre)/3)
if(score>70 and score<100):
  print("A")
elif(score>60 and score<69):
  print("B")
elif(score>50 and score<59):
  print("C")
else:
          print("FAIL")