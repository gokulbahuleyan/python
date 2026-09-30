def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
        while (True):
            if (greater%x==0) and (greater%y==0):
                lcm = greater
            break
        greater += 1
    return lcm
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(lcm(a,b))

