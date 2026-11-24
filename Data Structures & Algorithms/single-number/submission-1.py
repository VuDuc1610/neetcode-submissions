class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #x^x = 0 and x^0 = x
        ans = 0
        for num in nums:
            ans ^= num
        return ans 