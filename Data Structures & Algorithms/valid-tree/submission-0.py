class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #create adjacency list (if != n - 1 edges then wrong)
        if len(edges) != n - 1:
            return False

        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(0)

        #check to see if it's 1 connected piece
        def dfs(node):
            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
        
        dfs(0)
        if len(visited) != n:
            return False
        
        return True