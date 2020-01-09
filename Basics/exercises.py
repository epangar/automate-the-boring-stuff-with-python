#############

spam =  ['a','b', 'c', 'd'] 
print (spam[int(int('3' * 2) / 11)]) # print spam[3], which equals 'd'
print (spam[-3]) # print spam[1], which equals 'b
print (spam[:3]) # print ['a', 'b', 'c']

#############

"""Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats' . But your func-
tion should be able to work with any list value passed to it."""

spam = ['apples', 'bananas', 'tofu', 'cats']

def modify_array(array):
  answer=''
  total = len(array)

  for i in range(0,total):
    if i < total-1:
      answer += array[i] + ', '
    
    else:
      answer += 'and ' + array[i]
  
  
  return answer

print (modify_array(spam))


#############

grid = [
  ['.', '.', '.', '.', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['.', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.'] 
]

#print grid[8][5]

# for i in range(0, len(grid)):
#   print (grid[i])


for i in range(0, 6):
  
  row = grid[i]
  
  
  for j in range(0, len(grid)):
    item = grid[j][i]
    print (item, end=" ")
  print("\n")



