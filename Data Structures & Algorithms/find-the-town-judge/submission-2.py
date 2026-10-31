class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        noJudge = [False]*(n+1)
        map = {}

        for l, r in trust:
            noJudge[l] = True
            if r not in map:
                map[r] = [l]
            else:
                map[r].append(l)
        
        for i in range(1, len(noJudge)):
            if not noJudge[i] and i in map and len(map[i]) == n-1:
                return i
        
        return -1
