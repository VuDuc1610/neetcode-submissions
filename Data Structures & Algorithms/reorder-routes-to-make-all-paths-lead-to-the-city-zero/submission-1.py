class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}

        graph={i:[] for i in range(n)}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        visit.add(0)
        count = 0
        stack = [0]

        while stack:
            cur = stack.pop()
            for neighbor in graph[cur]:
                if neighbor in visit:
                    continue
                if (neighbor, cur) not in edges:
                    count += 1
                visit.add(neighbor)
                stack.append(neighbor)
        return count