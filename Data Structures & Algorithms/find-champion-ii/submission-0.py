class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
       #build adjacency list
        # graph = {i:[] for i in range(n)}
        # for u, v in edges:
        #     graph[u].append(v)
       #having a set of weak team

       #whoever not in the set then thats the strongest team


        weak = set()
        for u, v in edges:
            weak.add(v)
        
        if len(weak) != n - 1:
            return -1
        
        for i in range(n):
            if i not in weak:
                return i