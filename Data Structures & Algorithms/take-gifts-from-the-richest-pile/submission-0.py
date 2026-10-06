class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for i in range(len(gifts)):
            heapq.heappush(heap, -gifts[i])
        
        while k > 0:
            raw = -heapq.heappop(heap)
            curr = isqrt(raw)
            heapq.heappush(heap, -curr)
            k -= 1
        return -sum(heap)