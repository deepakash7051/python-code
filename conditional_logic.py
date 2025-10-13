is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive')
elif is_licenced:
    print('You can drive now')
else:
    print('checkcheck')

if is_licenced and is_licenced:
    print('You are old enough to drive and you have licence!')

# Truthy and Falsy
is_old = 'hello'
is_licenced = bool(5)

if is_old:
    print('You are old enough to drive')
elif is_licenced:
    print('You can drive now')
else:
    print('checkcheck')

if is_licenced and is_licenced:
    print('You are old enough to drive and you have licence!')

# Ternary Operator (short hand way to do if and else conditions)
# condition_if_true if condition else condidtion_if_false
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to messages"
print(can_message)


# check if magician and expert, you are master magician.
# check if you are magician but not expert, at least you're there.
# if you are not magician, you need magic powers

is_magician = False
is_expert = False

if is_magician and is_expert:
    print("You are a expert magician")
elif is_magician and not is_expert:
    print("at least you are there")
elif not is_magician:
    print("You need magic powers")

# comparision operators
# print(True == 1)
# print('1' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

# is - is actually check the location in memory - where they actually stored
print(True is 1)
print('1' is '1')
print([] is 1)
print(10 is 10.0)
print([] is [])

# Loops
for item in 'hail hydra':
    print(item)

for item in [1,2,3]: # list
    print(item)

for item in {1,2,3}: # set
    print(item)

for item in (1,2,3): # tuple
    print(item)
print(item)

# loop nesting
for item in (1,2,3,4,5):
    for x in ['a','b','c','d']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string
# iterate - one by one check each item in the collection.

# loop on dictionary
user = {
    'name': "Akash",
    'age':33,
    'can_fight':True
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, values = item
    print(key, values)

for key, values in user.items():
    print(key, values)

# for item in 50:
#     print(item)

#counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for i in my_list:
    counter += i
print(counter)

# range - create a special kind on object that we can itrate over
for num in range(0,10):
    # print( num )
    print("email sent list")

for num in range(0,10, 2):
    print( num )

for num in range(10, 0, -1):
    print( num )

# Enumerate - gives you iteratable object in index
for i,enumerate in enumerate('hellooo'):
    print(i,enumerate)

# for i, char in enumerate(list(range(100))):
#     print(i, char)

# while loop
# while condition:
i = 0
# while i <= 50:
#     print(i)
#     i += 1
#     break
# else:
#     print("done with all the work")

# break and continue
# while i <= 50:
#     # continue
#     # print(i)
#     # i += 1
# else:
#     print("done with all the work")

#pass
# while i <= 50:
#     pass
# pattern
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*',end="")
        else:
            print(' ',end="")
    print('')

# check duplicate in the list
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
    # check = some_list.count(value)
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)