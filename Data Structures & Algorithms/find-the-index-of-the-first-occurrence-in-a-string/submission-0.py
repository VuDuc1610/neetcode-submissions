class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def match(h, n):
            if len(h) != len(n):
                return False
            for i in range(len(h)):
                if h[i] != n[i]:
                    return False
            return True
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if match(haystack[i:i+len(needle)], needle):
                    return i
        return -1