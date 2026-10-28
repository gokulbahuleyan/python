#check the 2 lists are of same length.
print("to check the 2 lists are of same length")
print()

list1=[1,2,3,4,5]
list2=[1,2,3,4,6]
print("the first list:" + str(list1))
print("the second list:" + str(list2))
l1=len(list1)
l2=len(list2)
print("length of list1:",l1,"and length of list2:",l2)
if l1 == l2:
    print("list are same length")
else:
    print("list are of different length")

#check its sums.
print()
print("to check its sums")
print()

list1=[1,2,3,4,5]
list2=[1,2,3,4,6]
print("the first list is:" + str(list1))
print("the second list is :" + str(list2))
sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("the sum of all the numbers is:",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("the sum of all the numbers is:",sum2)
if sum1==sum2:
    print("list sum to same value")
else:
    print("list sum to different value")

#check the same values are occured in both
print()
print("check the values occured in both")
print()

list1=[1,2,3,4,5]
list2=[1,2,3,4,6]
print("the first list is:" + str(list1))
print("the second list is:" + str(list2))
print("the values occur in both lists:")
for x in list1:
    if (x in list1 and x in list2):
        print(x)

