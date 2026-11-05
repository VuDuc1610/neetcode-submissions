class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            parents[root_a] = root_b
            return True
            
        ans = len(isConnected)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    if union(r, c):
                        ans -= 1
        
        return ans
        
