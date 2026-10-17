class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (dist,[x,y]))

        while k > 0:
            _, res = heapq.heappop(heap)
            ans.append(res)
            k -= 1
        
        return ans