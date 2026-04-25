class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x!= 0):
            return False
        k = 0
        while x > k:
            k = k*10+x%10
            x //= 10
        return x ==k or x ==k//10