# Dictionary

dictionary = {
    'a':1,
    'b':2,
    'c':[1,2,3]
}

print(dictionary)
print(dictionary['c'][2])

# Why do we need dictionary
# Why do we need List

'''
    A dictionary has no order, a list has order
    May you wanna list of people online on your shop - you should probably use a list.
    But may be you have a user that playing a game, has information like name, age - that doesn't have to be ordered.
    Dictionary holds the more infomation than a list.
    Deep down a list is simply a index some sort of values.
'''

# Dictionary Keys
dict_ = {
    123:[123],
    True:'hello',
    # [100]: True # Type Error - unhashable type
}

# Dictionary keys need to have a special property - A key needd to be immutable i.e a key cannot change.

dict_2 = {
    '123' : [1,2,3],
    '123': 'hello'
}

print(dict_2['123'])
''' A key in dictionary has to be uniue because there can only be one key because the key is gping to be represent a bookshelf in that memory space '''

# Dictionary methods

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

# print('basket' in user)

# key
# print('gender' in user.keys())

# values
# print('hello' in user.values())

# item - grab all item
# print(user.items())

# clear
# user.clear()
# print(user)

# copy
# user_2 = user.copy()
# print(user_2)

# pop
# user.pop('age')
# print(user)

# popitem
# print(user.popitem())

#update
user.update({'age':33})
print(user)