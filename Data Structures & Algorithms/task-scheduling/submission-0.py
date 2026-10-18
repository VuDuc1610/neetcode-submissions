class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)
        for letter, count in count.items():
            heapq.heappush(heap, (-count, letter))
        
        waiting = deque()
        time = 0

        while heap or waiting:
            if waiting and waiting[0][2] == time:
                char, cnt, _ = waiting.popleft()
                heapq.heappush(heap, (cnt, char))
            
            if heap:
                cnt, char = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    waiting.append((char, cnt, time + n+1))

            time += 1
        
        return time
            
