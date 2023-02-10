#prog to print on the salary and the years of service with the bonus amount
salary=int(input("enter the salary of the employee :"))
yos=int(input("years of service :"))

if(yos>10):
    net_bonus=0.1*salary
    print("net bonus is ", net_bonus)
elif(yos>=6 and yos<=10):
    net_bonus=0.08*salary
    print("net bonus is ", net_bonus)
elif(yos<6): 
    net_bonus=0.05*salary
    print("net bonus is", net_bonus)
else:
    print("no net bonus")