class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bucket = [0]*len(nums)
        for i in range(len(nums)):
            bucket[nums[i]-1] = 1
        ans = []
        for i in range(len(bucket)):
            if bucket[i] == 0:
                ans.append(i+1)
        return ans