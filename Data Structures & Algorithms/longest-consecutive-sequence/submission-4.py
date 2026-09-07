class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        
        ans = 0
        for num in mySet:
            temp = 0
            if num - 1 not in mySet:
                temp = 1
                while num + 1 in mySet:
                    temp += 1
                    num += 1
                ans = max(ans,temp)
        return ans
