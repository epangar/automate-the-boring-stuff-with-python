import copy

# Copy
mylist = [1,2,3,4,5,6]

second_list = copy.copy(mylist)

print (second_list)


# Deep Copy

mylistoflists = [
  [
    [1,2],
    [3,4]
  ],
  [
    [5,6],
    [7,8]
  ]
]

a = copy.deepcopy(mylistoflists)

print(a)