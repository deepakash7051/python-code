# function allow us to keep our code DRY.

#default parameters
def say_hello():
    print("hello world")

say_hello()

# parameters and arguments
def greetings(name="Ram", greet="Good Morning"):
    print(f"Hello! {name}, {greet}")

greetings()

# greetings("Akash", "Good Evening")

# Default parameters and keyword arguments

#positional arguments
greetings("Akash", "Good Evening")

#keyword arguments
greetings(greet="Good Night",name="Akash")

# return - keyword in python that return some data
def sum(num1, num2):
    return num1 + num2

print(sum(2,2))

total = sum(520,660)
print(total)

def add(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = add(10, 20)
print(total)

# Methods and functions
# Build in function in python
'''
    list()
    print()
    max()
    min()
    input() '''

# methods - methodsa are own by somthing (start with .)
print('hello'.capitalize())

# Decstrings
def test(a):
    '''
        Info: this function tests and print a params
    '''
    print(a)
test('helloo')

# help inbulid function
help(test(1))

# magic method __doc__
print(test.__doc__)

# *args **kwargs

def super_func(*args, **kwargs):
    print(*args)
    print(kwargs)
    # return sum(args)
super_func(1,2,3,4,5, num1=1,num2=10)

# rule: params, *args, default, parameters, **kwargs

# Walrus Operator
''' := assign value to variable as part of large expresion'''

a = 'hellooooooooooo'
if len(a) > 10:
    print(f"too long {len(a)} elements")

# walrus - :=
if ( (n := len(a)) > 10):
    print(f"too long {n} elements")

while( (n := len(a)) > 1 ):
    print(n)
    a = a[:-1]
print(a)

# scope - what variable di I have access to?
# print(name())

a = 1

def confusion():
    a = 5 # local scope
    return a

print(a)
print(confusion())