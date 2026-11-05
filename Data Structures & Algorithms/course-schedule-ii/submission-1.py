class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create a directed adjacency list first
        graph = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
        
        visit = set()
        done = set()
        ans = []
        #create dfs function
        def dfs(node):
            if node in done:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            done.add(node)
            ans.append(node)
            return True

        #create a loop to for all of the numCourses
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans