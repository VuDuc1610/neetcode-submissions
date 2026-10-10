class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:]
        ans = 0
        strNum = str(num)
        for i in range(len(strNum)):
            if strNum[i] == "1":
                ans += 1
        return ans 