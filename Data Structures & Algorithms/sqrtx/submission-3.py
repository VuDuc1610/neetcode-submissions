class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x

        while l < r:
            m = l + (r-l)//2

            if m*m > x:
                r = m
            else:
                l = m + 1
        
        return l-1