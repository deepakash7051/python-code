class PlayerCharacter:
    #Attribute
    membership = True
    def __init__(self, name):
        if (self.membership):             
            self.name = name
    # Method
    def run(self):
        print('run')

obj = PlayerCharacter('Akash')
print(obj.name)
print(obj.run())


class SumOfVegetables:
    price = [100, 180, 80, 130, 40, 30]

    def __init__(self):
        self.total = sum(self.price)  # better and cleaner way

    def __str__(self):
        return f"Total price of vegetables: {self.total}"
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

obj = SumOfVegetables()
print(obj)

# no need to create the instance of the class
print(SumOfVegetables.adding_things(10,20))

class User:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def detail(self): #Abstract way to handle data
        print(f'my name is {self.name} and I\'m {self.age} year old')

user = User('akash',33)
print(user.detail())

# Encapsulations
# Encapsulation is the binding of the data and manulating that data.

#Abstraction
# Hiding of information or abstracting away of information and giving access to only what's necessary.
