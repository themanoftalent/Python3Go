# init is initilaizing
'''self as it suggests, refers to itself- the object which has called the method.
That is, if you have N objects calling the method, then self.a will refer to a separate
instance of the variable for each of the N objects. Imagine N copies of the variable a for each object
__init__ is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is
 that it is a special method which is automatically called when an object of that Class is created
'''


class Person:
    '''Doc - Inside Class '''

    def __init__(self, name):
        '''Doc - __init__ Constructor'''
        self.n_name = name

    def show(self, number1, number2):
        '''Doc - Inside Show'''
        # print (self.n_name)
        print('Sum = ', (number1 + number2))
        return 'Sum = ', (number1 + number2)

    def __del__(self):
        print('Destructor Deleting object - ', self.n_name)


p = Person('Jay')
print(p.n_name, end=", ")
p.show(2, 3)
# print("\nThis returns the func ", p.show(2, 3))

p2 = Person('Halil')
print(p2.n_name, end=", ")
p2.show(12, 13)

print("\nExtra info ")
print(p.__doc__)
print(p.__init__.__doc__)
print(p.show.__doc__)
