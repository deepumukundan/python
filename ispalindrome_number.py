class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            print(reversed)
            x //= 10
            print(x)

        print(f'Final reversed: {reversed}')
        return x == reversed or reversed // 10 == x

sol = Solution()
print(sol.isPalindrome(121))