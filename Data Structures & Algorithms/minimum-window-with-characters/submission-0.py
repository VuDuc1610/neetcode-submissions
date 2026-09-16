class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapt, maps, count, need, minLen, idx, ptr = {},{},0,0,float('inf'),[-1,-1],0
        for char in t:
            mapt[char] = 1 + mapt.get(char,0)
        need = len(mapt)

        for i in range(len(s)):
            char = s[i]
            maps[char] = 1 + maps.get(char,0)
            if char in mapt and maps[char] == mapt[char]:
                count += 1
            while count == need:
                if i - ptr + 1 < minLen:
                    idx = [ptr,i]
                    minLen = i - ptr + 1
                maps[s[ptr]] -= 1
                if s[ptr] in mapt and maps[s[ptr]] < mapt[s[ptr]]:
                    count -= 1
                ptr += 1
        if minLen == float('inf'):
            return ""
        return s[idx[0]:idx[1]+1]
            
