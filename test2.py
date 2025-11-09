import random
num=[0,1,3,2,6,8,7,4,5,10,9]
target=int(input("enter the target number below 10: "))
while True:
    num1=random.randint(num[0],num[10])
    num2=random.randint(num[0],num[10])
    c=num1+num2
    ind1=num1
    ind2=num2
    if c==target:
        print("index is","[",num.index(ind1),",",num.index(ind2),"]","in list",num)
        print(f"{num1} + {num2} = {c}")
        break 
    elif c!=target:
        continue
    break


