def binary_search(arr: list, x: int):
    low, high = 0, len(arr) - 1
    
    count = 0
    while low <= high:
        mid = low + (high - low) // 2
        count += 1

        current = arr[mid]
        print(f"Found {current} at index {mid}")
        if current == x:
            return True, count
        elif x > current:
            low = mid + 1
        else:
            high = mid - 1
    
    return False, count


arr1 = [i for i in range(10000000)]
print(binary_search(arr1, 50))