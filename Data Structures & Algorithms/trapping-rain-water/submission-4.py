class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [],[]
        ans, tempL, tempR = 0,0,0
        for num in height:
            if num > tempL:
                tempL = num
            left.append(tempL)
        for num in reversed(height):
            if num > tempR:
                tempR = num
            right.append(tempR)
        right.reverse()
            
        for i in range(len(height)):
            ans += min(left[i],right[i])-height[i]
        return ans
            