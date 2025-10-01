"""
Pythonic Sorting Algorithms: From Worst to Best Average Performance
================================================================

Big O Complexity Table:
┌─────────────────┬─────────────┬─────────────┬─────────────┬───────────────┐
│ Algorithm       │ Best Case   │ Average     │ Worst Case  │ Space         │
├─────────────────┼─────────────┼─────────────┼─────────────┼───────────────┤
│ Bubble Sort     │ O(n)        │ O(n²)       │ O(n²)       │ O(1)          │
│ Selection Sort  │ O(n²)       │ O(n²)       │ O(n²)       │ O(1)          │
│ Insertion Sort  │ O(n)        │ O(n²)       │ O(n²)       │ O(1)          │
│ Shell Sort      │ O(n log n)  │ O(n^1.25)   │ O(n²)       │ O(1)          │
│ Heap Sort       │ O(n log n)  │ O(n log n)  │ O(n log n)  │ O(1)          │
│ Merge Sort      │ O(n log n)  │ O(n log n)  │ O(n log n)  │ O(n)          │
│ Quick Sort      │ O(n log n)  │ O(n log n)  │ O(n²)       │ O(log n)      │
│ Tim Sort        │ O(n)        │ O(n log n)  │ O(n log n)  │ O(n)          │
└─────────────────┴─────────────┴─────────────┴─────────────┴───────────────┘
"""

import heapq
from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(arr: List[T]) -> List[T]:
    """
    Bubble Sort: O(n²) average case
    Most inefficient but simple to understand
    """
    arr = arr.copy()  # Don't mutate original
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Pythonic swap
                swapped = True
        
        if not swapped:  # Early termination optimization
            break
    
    return arr


def selection_sort(arr: List[T]) -> List[T]:
    """
    Selection Sort: O(n²) all cases
    Consistently poor performance
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = min(range(i, n), key=lambda x: arr[x])  # Pythonic min finding
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[T]) -> List[T]:
    """
    Insertion Sort: O(n²) average, O(n) best case
    Good for small or nearly sorted arrays
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def shell_sort(arr: List[T]) -> List[T]:
    """
    Shell Sort: O(n^1.25) average case
    Improvement over insertion sort using gap sequences
    """
    arr = arr.copy()
    n = len(arr)
    
    # Using Knuth sequence: 1, 4, 13, 40, 121, ...
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    
    while gap >= 1:
        # Gap insertion sort
        for i in range(gap, n):
            key = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = key
        
        gap //= 3
    
    return arr


def heap_sort(arr: List[T]) -> List[T]:
    """
    Heap Sort: O(n log n) all cases
    Uses Python's heapq module for Pythonic implementation
    """
    # heapq creates min-heap, but we want max-heap for ascending sort
    # So we negate values, heapify, then negate back
    heap = [-x for x in arr]
    heapq.heapify(heap)
    
    return [-heapq.heappop(heap) for _ in range(len(heap))]


def merge_sort(arr: List[T]) -> List[T]:
    """
    Merge Sort: O(n log n) all cases, O(n) space
    Stable, predictable performance
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[T], right: List[T]) -> List[T]:
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Extend with remaining elements (Pythonic)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[T]) -> List[T]:
    """
    Quick Sort: O(n log n) average, O(n²) worst case
    Very fast in practice with good pivot selection
    """
    if len(arr) <= 1:
        return arr.copy()
    
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    
    # Pythonic partitioning using list comprehensions
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def tim_sort(arr: List[T]) -> List[T]:
    """
    Tim Sort: O(n log n) average, O(n) best case
    Python's built-in sort - hybrid of merge sort and insertion sort
    Optimized for real-world data patterns
    """
    # This is what Python's sorted() and list.sort() use internally
    return sorted(arr)


# Alternative Pythonic quick_sort with in-place partitioning
def quick_sort_inplace(arr: List[T]) -> List[T]:
    """
    In-place Quick Sort: More memory efficient
    """
    arr = arr.copy()
    
    def _quick_sort_helper(arr: List[T], low: int, high: int) -> None:
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort_helper(arr, low, pi - 1)
            _quick_sort_helper(arr, pi + 1, high)
    
    def partition(arr: List[T], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


# Demonstration and benchmarking
if __name__ == "__main__":
    import time
    import random
    
    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    large_data = [random.randint(1, 1000) for _ in range(100)]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort), 
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Heap Sort", heap_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Tim Sort (built-in)", tim_sort),
    ]
    
    print("Testing with small array:", test_data)
    print("=" * 50)
    
    for name, func in algorithms:
        start_time = time.perf_counter()
        result = func(test_data)
        end_time = time.perf_counter()
        
        print(f"{name:20}: {result}")
        print(f"{'':20}  Time: {(end_time - start_time)*1000:.4f}ms")
        print()
    
    # Performance comparison on larger dataset
    print(f"\nPerformance on {len(large_data)} random integers:")
    print("=" * 50)
    
    for name, func in algorithms:
        start_time = time.perf_counter()
        result = func(large_data)
        end_time = time.perf_counter()
        
        print(f"{name:20}: {(end_time - start_time)*1000:.2f}ms")