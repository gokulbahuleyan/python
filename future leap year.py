y=int(input('Enter a year:'))
print("future leap year form 2024:")
for i in range(2024,y+1):
    if (i%4==0) and (i%100!=0) or (i%400==0):
      print(i)
