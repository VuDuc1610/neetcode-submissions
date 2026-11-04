class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        
        #create adjacency list
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for l,r in edges:
            graph[l].append(r)
            graph[r].append(l)
        #dfs function

        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        #for loop to count connected components
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
