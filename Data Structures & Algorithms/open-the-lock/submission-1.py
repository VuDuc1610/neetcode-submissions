class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        count = 0
        visit = set()
        q = deque()
        q.append("0000")

        while q:
            check = False
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return count
                for i in range(len(cur)):
                    up = (int(cur[i]) + 1) % 10
                    down = (int(cur[i])-1) % 10
                    tmpUp = cur[:i] + str(up) + cur[i+1:]
                    tmpDown = cur[:i] + str(down) + cur[i+1:]

                    if tmpUp not in visit and tmpUp not in deadends:
                        q.append(tmpUp)
                        visit.add(tmpUp)
                        check = True
                    if tmpDown not in visit and tmpDown not in deadends:
                        q.append(tmpDown)
                        visit.add(tmpDown)
                        check = True
            if not check:
                return -1 
                    
            count += 1
        
        
        return count
                    
                    

