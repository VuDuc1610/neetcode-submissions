class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx, temp = 0, float('inf')
        for i in range(len(nums)):
            if abs(nums[i]) < temp:
                idx = i
                temp = abs(nums[i])
   
        ans = [nums[idx]*nums[idx]]
        left, right = idx - 1, idx + 1

        while left >= 0 or right < len(nums):
            if left < 0:
                ans.append(nums[right]*nums[right])
                right += 1
            elif right >= len(nums):
                ans.append(nums[left]*nums[left])
                left -= 1
            else:
                if abs(nums[left]) <= abs(nums[right]):
                    ans.append(nums[left]*nums[left])
                    left -= 1
                else:
                    ans.append(nums[right]*nums[right])
                    right += 1
        return ans