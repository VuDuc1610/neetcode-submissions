class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()

        if len(pattern) != len(lst):
            return False

        map = {}

        for i in range(len(pattern)):
            char = pattern[i]
            if char in map:
                if lst[i] != map[char]:
                    return False
            else:
                if lst[i] in list(map.values()):
                    return False
                map[char] = lst[i]
        return True
            