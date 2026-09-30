a=int(input("enter the number"))
num=0

if a>0:
    print(a)
else:
    print("give a number greater than 0")

while (a>0):
    num=num+1
    a=a//10
print(num)
