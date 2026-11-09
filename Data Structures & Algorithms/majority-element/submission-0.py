class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        max = 0
        ans = 0
        for key, val in map.items():
            if val > max:
                max = val
                ans = key
        
        return ans