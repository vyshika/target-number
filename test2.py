num=(input("enter a list of numbers")).split()
num=[int(x) for x in num]
print(num)
target=int(input("target number:"))
i=0
while i < (len(num)):
    j=i+1
    while j < (len(num)):
        result=num[i]+num[j]
        if result == target:
            print(num[i] ,"+",num[j])
            print("index :",i,j)
        j+=1
    i+=1


