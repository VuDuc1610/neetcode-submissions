import sys
sys.setrecursionlimit(20000)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visit = set()
        ans = []

        def dfs(node):
            if node in visit:
                return False
            if graph[node] == []:
                return True
            visit.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            graph[node] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        
        return ans
