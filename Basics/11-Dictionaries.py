import pprint #import prety print


spam = {
    'color': 'red', 
    'age': 42, 
    'foods': ['eggs', 'ham', 'peanuts']
    }

# .keys()

for a in spam.keys():
  print(a)

# .values()

for g in spam.values():
  print(g)

# .items()

for v in spam.items():
  print(v)

print ( 'color' in spam ) #True
print ( 'glasses' in spam ) #False

#####  get()


picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing 2 cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
print('I am bringing 0 eggs.')


#  setdefault() 

# You’ll often have to set a value in a dictionary for a certain key only if that
# key does not already have a value. The code looks something like this:
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# The setdefault() method offers a way to do this in one line of code. The
# first argument passed to the method is the key to check for, and the second
# argument is the value to set at that key if the key does not exist. If the key
# does exist, the setdefault() method returns the key’s value. Enter the following into 
# the interactive shell:

spam = {'name': 'Pooka', 'age': 5}
print (spam)
spam.setdefault('color', 'black')

print (spam)
#{'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')

print (spam)
#{'color': 'black', 'age': 5, 'name': 'Pooka'}



message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint (count) #pretty print

