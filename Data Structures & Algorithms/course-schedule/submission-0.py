class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a map which store key and the list of prereq first
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for l, r in prerequisites:
            preMap[l].append(r)

        visit = set()
        
        #create dfs function
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for preCrs in preMap[crs]:
                if not dfs(preCrs):
                    return False
            visit.remove(crs)
            preMap[crs] = []

            return True
                
        #create loop to check dfs for each nodes

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True