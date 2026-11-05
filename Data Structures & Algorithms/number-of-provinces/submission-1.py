class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = set()
        parents = [i for i in range(len(isConnected))]

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return
            parents[root_a] = root_b
        
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    union(r, c)
        
        for i in range(len(parents)):
            province.add(find(i))
        return len(province)
