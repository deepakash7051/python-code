#Fundamental datatypes
print(type(2+1))
print(type(2-1))
print(type(2*1))
print(type(2/1))
print(type(0))

print(2**3) #2's power of 3
print(5//4) #quationt
print(6 % 4) # remainder

#math functions
print('Math functions.')
print(round(3.9))
print(abs(-20)) #absolute value, positve number

#Developer Fundamentals
print('Developer Fundamentals')

#Operator precedence
print('Operators precedence')
# 1. ()
# 2. **
# 3. * /
# 4. + -

print(20 + 3 * 4);
print(20 - 3 * 4);

# Variables
iq = 190
print(iq)

# Ways to create variables
# 1. Snake Case: snake_case

user_iq = 190
# 2. Start with lowercase or underscore
userIQ = 190
# 3. Letters, numbers, underscores
useIQ190 = 190
# 4. Case sensitives
userIQ = 120
UserIQ = 130

# 5. Don't overwrite keywords


#another way to create a variable
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# Expression and statement
#express
iq=195

#statement
user_age = iq / 5

#augmented assignment operator
some_value = 5
some_value = some_value + 2

# now augmented assignment operator
some_value += 2
print(some_value)
# similarly
some_value -= 5
print(some_value)


#string
print(type("do not give up!"))

username = 'akash@yopmail.com'
password = 'admin123'
long_string = '''
WOW
0 0
---
'''
print(long_string)

firstname = 'Akashdeep'
lastname = 'Gautam'
fullname = firstname+' '+lastname
print(fullname)

# Type Convervsion
print('Type Conversion')
print(type(str(100)))

# Escape Sequence
weather = 'It\'s sunny'
print(weather)

#Formatted strings
print('Formtted strings')

name = 'John Doe'
age = 32

print(f'Hello {name}, you are {age} year old')

print('Hi {}, you are {} years old'.format('Akash',32))

# String Index
selfish = 'me me me'
print(selfish[3])

# [start:stop]
str = "01234567"
print(str[0:2])

# [start: end: stepover]
print(str[1:8:2])
print(str[1:])
print(str[:5])
print(str[::1])
print(str[-1])
print(str[::-1])
print(str[-2])
print(str[::-2])

# immutability (can not be chnage)
strg = '13213213212'
print(strg)
# strg[2] = 5
# print(strg)

# Some in build functions
print( len('helloooo') )

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)

# Booleans (TRUE/FALSE)
name = 'Andrei'
is_cool = False
is_cool = True
print(name)


birthYear = input('What is your birth year ')
age = 2025 - int(birthYear)

print(f'Your age is {age}')

# password checker
username = input('Username: ')
password = input('Password: ')

secret = '*' * len(password)

print(f"Hey {username}! your password {secret} is {len(password)} lettars long")

