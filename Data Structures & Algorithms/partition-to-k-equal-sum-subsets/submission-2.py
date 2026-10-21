class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target  = total//k
        bucket = [0]*k
        nums.sort(reverse=True)

        def helper(idx):
            if idx == len(nums):
                return True
            
            if nums[idx] > target:
                return False
            
            for i in range(len(bucket)):
                if bucket[i] + nums[idx] <= target:
                    bucket[i] += nums[idx]
                    if helper(idx+1):
                        return True
                    bucket[i] -= nums[idx]
                    if bucket[i] == 0:
                        break
            
            return False
            
        return helper(0)
