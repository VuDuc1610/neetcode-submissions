class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base, window, best = 0,0,0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
            else:
                window += customers[i]
            if i >= minutes and grumpy[i-minutes] == 1:
                window -= customers[i-minutes]
            if i >= minutes - 1:
                best = max(best, window)
        return base + best