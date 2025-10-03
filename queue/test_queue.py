from collections import deque

def test():
    q = deque([1,2,3,4])
    while q:
        print(q.popleft())

test()