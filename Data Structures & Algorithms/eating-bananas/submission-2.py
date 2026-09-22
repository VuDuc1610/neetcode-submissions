class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #because h is always greater or equal to len(piles)
        #=> max k only needs to be equal to max(piles)
        #the slowest k is 1 of course
        #=> idea is to iterate over from 1 to k to find the smallest number
        maxPile = max(piles)
        i, j = 1, maxPile+1
        res = 0
        while i < j:
            m = i + (j-i)//2
            ans = 0
            for num in piles:
                ans += -(-num//m)
            if ans <= h:
                res = m
                j = m
            else:
                i = m + 1
        return res
