# Tuples
#Tuples are just immutable lists. Use () instead of []

x = (1, 2, 3)
print(len(x))

y = (4, 5, 6)
print(y[2])

listOfTuples = [x, y]
print(listOfTuples)

(age, money) = "25,12000".split(',')
print("my age "+age+" and my salary "+money)
