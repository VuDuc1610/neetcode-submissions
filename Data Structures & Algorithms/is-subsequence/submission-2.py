class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        ps = 0
        for i in range(len(t)):
            if t[i] == s[ps]:
                ps += 1
                if ps == len(s):
                    return True
        return False