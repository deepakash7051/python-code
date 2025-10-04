# Set
''' 
    Sets are simply an unordered collection of unique objects
'''
my_set = {1,2,3,4,4,5,5,5}
print(my_set)

my_set.add(100)
my_set.add(2)
print(my_set)
print(2 in my_set)

# convert a list into set
my_list = [1,2,3,4,4,5,5,5]
print(set(my_list))

# set does not support indexing
print(my_set[2])