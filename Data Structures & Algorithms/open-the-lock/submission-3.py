class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        count = 0
        visit = set(deadends)
        if "0000" in visit:
            return -1
        visit.add("0000")
        q = deque(["0000"])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return count
                for i in range(len(cur)):
                    for d in (-1,1):
                        num = (int(cur[i]) + d) % 10
                        tmpLock = cur[:i] + str(num) + cur[i+1:]

                        if tmpLock not in visit:
                            q.append(tmpLock)
                            visit.add(tmpLock)
                            check = True
            count += 1
        
        
        return -1
                    
                    

