# List
""" List are like arrays """
li = [1,2,3,4,5]

li2 = ['a','b','c']

li3 = [1,2,'a',True]


amazon_cart = [
                'notebook',
                'sunglasses',
                'toys',
                'grapes'
                ]

# List Slicing
print(amazon_cart[0::2])

# List are mutable
amazon_cart[1] = 'Tv'
print(amazon_cart)

# I want item from index 1 to 3
print(amazon_cart[1:3])

# Matrix
'''This type of array comes most in machine learning'''
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

print(matrix[0][1])

# List methods
basket = [1,2,3,4,5]

#append
basket.append(100)
new_basket = basket
print(new_basket) # Everything in python is an object

#insert
new_list = basket.insert(5,10)
print(basket)
print(new_basket)

#extend
new_list = basket.extend([100,101])
print(basket)
print(new_list)

#pop
basket.pop()
basket.pop(0) # remove from index 0
print(basket)

# remove
basket.remove(100) # remove the value, we wanna remove
print(basket)

#clear
new_list = basket.clear() # clear removes, whatever in the list
print(basket)

# Common List pattern
cart = ['a','b','c','d','x','z']
cart.sort()
# cart.reverse()
print(cart)
print(cart[::-1])

#range
print(list(range(1,100)))
print(list(range(100)))

#join - something working on string
sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','jojo'])
print(new_sentence)

# list unpacking
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

a,b,c,*other, d = [1,2,3,4,5,6,7,8,9] 
print(a)
print(b)
print(c)
print(other)
print(d)