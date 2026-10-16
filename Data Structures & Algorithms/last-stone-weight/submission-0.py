class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            num1 = -heapq.heappop(stones)
            num2 = -heapq.heappop(stones)
            curr = num1-num2
            heapq.heappush(stones, -curr)
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        return 0