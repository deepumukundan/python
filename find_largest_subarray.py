def find_largest_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr)

    return ans

ans = find_largest_subarray([30,2,3,4,5,6,7,8,9,10], 3)
print(ans)