a = {i: i*2 for i in range(10)}
print(a)

a.pop(9)
print(a)

for key, val in a.items():
    print(key, val)