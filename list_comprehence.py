#genereate a positive list of numbers form a given list of integers

print("positive list of integers")
print()

mylist=[23,58,-12,90,-45,81,49,-36]
print("first list:",mylist)
newlist=[x for x in mylist if x<0]
print("second list:",newlist)

#square of the given numbers
print("square of n numbers")
print()

mylist=[2,5,3,8]
print("first list:",mylist)
newlist=[number ** 2 for number in mylist]
print("second list:",newlist)

#select the vowels from the given word
print("select vowels from the word")
print()

word=input("enter a word")
vowels=['a','e','i','o','u']
list=[]
for x in word:
    if (x in vowels and x not in list):
        list.append(x)
print("vowel present in the given word is:", list)

#list ordinal values of each element of a word
print("list ordinal values")
print()

a=input("enter a word")
for i in range(len(a)):
    print("ascii values is" ,a[i],"is", ord(a[i]))


