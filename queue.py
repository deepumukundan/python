from collections import deque

a = deque()
for i in [2,1,3,4,6,9]:
    a.append(i)
print(a)
print(a.popleft())
print(a)
print(a.pop())
print(a)