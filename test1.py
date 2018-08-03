# Functions

def SquareIt(x):
    return x * x

print (SquareIt(3))

#You can pass functions around as parameters

def DoSomething(function, x):
    return function(x) + x
    pass

print(DoSomething(SquareIt, 4))

#Lambda functions let you inline simple functions

#print(DoSomething(Lambda x: x * x * x, 3))
print(DoSomething(lambda x: x * x * x, 3))
