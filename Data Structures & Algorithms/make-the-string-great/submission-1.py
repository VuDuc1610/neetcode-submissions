class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            cur = s[i]
            if stack and abs(ord(cur)-ord(stack[-1])) == 32:
                stack.pop()
                continue
            stack.append(cur)
        
        ans = "".join(stack)
        return ans

