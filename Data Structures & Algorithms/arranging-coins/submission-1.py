class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans, cnt, tmp = 0, 0, 1

        while True:
            cnt += tmp
            if cnt > n:
                break
            ans += 1
            tmp += 1
        
        return ans