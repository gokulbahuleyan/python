a=int(input("enter the number"))
b=a
sum=0
while a>0:
    sum=(sum*10)+(a%10)
    a=a//10
if sum==b:
    print("this number is palindrom")
else:
    print("this number is not palindrom")