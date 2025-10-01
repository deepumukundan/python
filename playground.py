def hash(a, b):
    return a * 2 ** 32 + b

print(hash(1, 2))
print(hash(2, 1))
print(hash(1, 2) == hash(2, 1))
print(hash(1, 2) is hash(2, 1))
print(hash(1, 2) != hash(2, 1))
print(hash(1, 2) is not hash(2, 1))
print(hash(1, 2) < hash(2, 1))
print(hash(1, 2) > hash(2, 1))
print(hash(1, 2) == hash(1, 2))