class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ptr = 0
        if len(s2) < len(s1):
            return False
        map1,map2 = {},{}
        for i in range(len(s1)):
            map1[s1[i]] = 1 + map1.get(s1[i],0)
        for i in range(len(s2)):
            if i < len(s1)-1:
                map2[s2[i]] = 1 + map2.get(s2[i],0)
                continue
            map2[s2[i]] = 1 + map2.get(s2[i],0)
            if map1 == map2:
                return True
            map2[s2[ptr]] -= 1
            if map2[s2[ptr]] == 0:
                map2.pop(s2[ptr])
            ptr += 1
        return False
