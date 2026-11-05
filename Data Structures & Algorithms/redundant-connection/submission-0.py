class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        
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
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        
        
        return [-1,-1]
