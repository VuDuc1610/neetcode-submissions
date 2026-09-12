class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        i, j = 1, maxPile
        res = 0
        while i <= j:
            m = i + (j-i)//2
            ans = 0
            for num in piles:
                ans += -(-num//m)
            if ans <= h:
                res = m
                j = m - 1
            else:
                i = m + 1
        return res
