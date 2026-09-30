a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print(" +  addition")
print(" -  subtraction")
print(" *  multiplication")
print(" /  division")
print(" % modulus")
c=input("enter your choice:")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
else:
    print(c)

