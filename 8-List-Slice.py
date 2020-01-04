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