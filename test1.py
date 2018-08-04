# Looping

for x in range(10):
    print(x)
    pass

print("next")

for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print(x)

print("next")

x = 0
while (x < 10):
    print(x)
    x += 1
    pass
