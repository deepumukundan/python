lst1 = [1,2,3]
lst2 = [3,4,5]
print([x * y for x in lst1 for y in lst2])

print(any(i % 3 for i in [3,3,4,4,3]))

print(all(i % 3 for i in [3,3,4,4,3]))

print(sum(1 for i in [3,3,4,4,3] if i == 4))

del(lst1[0])
print(lst1)
del(lst1)