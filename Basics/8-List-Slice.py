mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print ('++++++++++\n')
for i in range(len(mylist)):
  print ('Index %r of this list is %r' % (i, mylist[i]))


print ('\n++++++++++\n')
for j in range(0, len(mylist)+1 ):
  for k in range(0, len(mylist)+1 ):
    if j <= k:
      print ('Showing mylist[%d:%d]: %r' % (j,k, mylist[j:k]))
    else:
      continue


print ('\n++++++++++\n')
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size, color, disposition)


print ('\n++++++++++\n')

list_of_cats = ["Cat"]

for i in range(0,5):
  print (list_of_cats * i)


print ('\n+++++ Methods +++++\n')

print ('\nIndex()\n')

for i in mylist:
  print (mylist.index(i))

print ('\nAppend() & Insert()\n')

newArray = ['', '-', '--']

for i in range(0,3):
  for j in range (0,3):
    newArray.append(i)
    newArray.insert(j,"*"*i)

print (newArray)

print ('\nSort()\n')

numbers = [0,1,9,2,8,3,7,4,6,5]

numbers.sort()
print (numbers)

numbers.sort(reverse = True)
print (numbers)

spam = ['a', 'z', 'A', 'Z', 'b','C','s','S']
spam.sort(key=str.lower)
print(spam)
spam.sort(key=str.upper, reverse = True)
print(spam)

print ('\nRemove()\n')

newArray.remove('--')

print (newArray)

print ('\nDel()\n')

print (len(newArray))
for i in range(0, len(newArray)):
  print (newArray, i)
  del newArray[20-i-1]

print (newArray)