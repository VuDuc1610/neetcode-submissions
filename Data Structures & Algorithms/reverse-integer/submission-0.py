class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31 
        res = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1
        while x != 0:
            cur = x % 10
            res *= 10
            res += cur
            x //= 10
        if  res < INT_MIN or res > INT_MAX:
            return 0
        if isNegative:
            return res*(-1)
        return res

