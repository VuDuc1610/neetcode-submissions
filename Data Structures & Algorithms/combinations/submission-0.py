class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(temp, cur):
            if len(temp) == k:
                ans.append(temp[:])
                return
            if cur > n:
                return
            temp.append(cur)
            helper(temp, cur+1)
            temp.pop()
            helper(temp,cur+1)
        
        helper([],1)
        return ans
