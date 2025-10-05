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