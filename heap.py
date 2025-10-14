import heapq

def min_heap():
    minheap = [9,1,3,8,4,7,0]
    print(minheap)
    heapq.heapify(minheap)
    print(minheap)
    print(type(minheap))

    print(heapq.heappop(minheap))
    print(minheap)
    print(heapq.heappop(minheap))
    print(minheap)

    while minheap:
        print(heapq.heappop(minheap))
        print(minheap)

def max_heap():
    
    maxheap = []
    for i in range(10):
        heapq.heappush(maxheap, -i)
    print(maxheap)

    print(-heapq.heappop(maxheap))
    print(maxheap)
    print(-heapq.heappop(maxheap))
    print(maxheap)

    while len(maxheap):
        print(-heapq.heappop(maxheap))
        print(maxheap)


print("----Min Heap----")
min_heap()
print("-----------------")
print("----Max Heap----")
max_heap()