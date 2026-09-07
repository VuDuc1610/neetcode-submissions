class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights) - 1
        while left < right:
            numL, numR = heights[left], heights[right]
            h = min(numL, numR)
            ans = max(ans, h*(right-left))
            if numL <= numR:
                left += 1
            else:
                right -= 1
        return ans