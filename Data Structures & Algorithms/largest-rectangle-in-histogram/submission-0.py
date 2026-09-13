class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)):
            if i == 0:
                stack.append([0,heights[0]])
            else:
                if heights[i] > stack[-1][1]:
                    stack.append([i,heights[i]])
                else:
                    tempIndex = i
                    while stack and heights[i] <= stack[-1][1]:
                        area = (i-stack[-1][0])*stack[-1][1]
                        ans = max(ans, area)
                        tempIndex = stack[-1][0]
                        stack.pop()
                    stack.append([tempIndex,heights[i]])
        while stack:
            area = (len(heights)-stack[-1][0])*stack[-1][1]
            ans = max(ans,area)
            stack.pop()
        return ans
