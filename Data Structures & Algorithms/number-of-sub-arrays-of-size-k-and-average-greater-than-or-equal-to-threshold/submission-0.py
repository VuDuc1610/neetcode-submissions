class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumNum = threshold*k
        ans,window = 0,0

        for i in range(len(arr)):
            window += arr[i]
            if i >= k:
                window -= arr[i-k]
            if i >= k-1 and window >=sumNum:
                ans += 1
        return ans