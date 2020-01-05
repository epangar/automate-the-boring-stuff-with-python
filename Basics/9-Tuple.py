""" The tuple data type is almost identical to the list data type, except in two
ways. First, tuples are typed with parentheses, ( 99 ) , instead of square
brackets, [ 99 ] .  """


eggs = ('hello', 42, 0.5)

print (eggs[0])
#equals 'hello'

print (eggs[1:3])
#equals (42, 0.5)

print (len(eggs))
#equals 3

tuple(['cat', 'dog', 5])
# equals ('cat', 'dog', 5)

list(('cat', 'dog', 5))
# equals ['cat', 'dog', 5]

list('hello')
# equals ['h', 'e', 'l', 'l', 'o']