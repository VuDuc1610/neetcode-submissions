class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, maxNum, minNum, l = 0, deque(), deque(), 0

        for i in range(len(nums)):
            while maxNum and nums[maxNum[-1]] < nums[i]:
                maxNum.pop()
            while minNum and nums[minNum[-1]] > nums[i]:
                minNum.pop()
            maxNum.append(i)
            minNum.append(i)

            while nums[maxNum[0]] - nums[minNum[0]] > limit:
                if nums[l] == nums[maxNum[0]]:
                    maxNum.popleft()
                if nums[l] == nums[minNum[0]]:
                    minNum.popleft()
                l += 1
            ans = max(ans, i - l + 1)
        
        return ans
                