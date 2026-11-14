class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l1, r1 = i,i
            l2, r2 = i, i + 1

            while l1 >= 0 and r1 <= len(s)-1:
                if s[l1] != s[r1]:
                    break
                count += 1
                l1 -= 1
                r1 += 1
            
            while l2 >= 0 and r2 <= len(s)-1:
                if s[l2] != s[r2]:
                    break
                count += 1
                l2 -= 1
                r2 += 1
        return count
                
                