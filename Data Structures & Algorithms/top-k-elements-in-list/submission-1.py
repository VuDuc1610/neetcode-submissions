class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num,0)
        
        tempHeap = []
        for num, curr in map.items():
            heapq.heappush(tempHeap, [curr,num])
        count = 0
        ans = []
        while tempHeap:
            if count < len(tempHeap) - k:
                heapq.heappop(tempHeap)
            else:
                ans.append(heapq.heappop(tempHeap)[1])
        return ans
