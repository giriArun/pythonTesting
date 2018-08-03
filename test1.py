# Lists

x = [1, 2, 3, 4, 5, 6]
print(len(x))
print(x[:3])
print(x[3:])
print(x[-4:])

x.extend([7, 8])
print(x)

x.append(9)
print(x)

y = [11, 22, 33]
listofLists = [x, y]
print(listofLists)

z = [52, 51 , 55]
z.sort()
print(z)

z.sort(reverse=True)
print(z)
