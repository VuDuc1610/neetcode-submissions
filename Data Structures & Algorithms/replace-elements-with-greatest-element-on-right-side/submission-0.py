class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        ans = [-1]
        for i in range(len(arr)-2, -1, -1):
            ans.append(maxNum)
            maxNum = max(maxNum, arr[i])
        return ans[::-1]