sys.setrecursionlimit(10000)
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if j == len(nums2) or i == len(nums1):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if nums1[i] == nums2[j]:
                ans = 1 + dp(i+1, j+1)
            else:
                ans = max(dp(i+1,j), dp(i,j+1))
            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)