class Solution:
    def check(self, arr, m, days):
        countDay, i, tempWeight = 0, 0, 0
        while i < len(arr):
            tempWeight += arr[i]
            if tempWeight <= m:
                i += 1
            else:
                countDay += 1
                tempWeight = 0
        if tempWeight > 0:
            countDay += 1
        return countDay


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r-l)//2
            count = self.check(weights, m, days)
            if count > days:
                l = m + 1
            else:
                r = m
        return l
            