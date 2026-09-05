class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num,0)
        temp = []
        for num, cur in map.items():
            temp.append([cur,num])
        temp.sort()
        ans = []
        while len(ans) < k:
            ans.append(temp.pop()[1])
        return ans
