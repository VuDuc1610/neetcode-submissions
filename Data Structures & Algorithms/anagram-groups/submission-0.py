class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        print(len(strs))
        if len(strs) == 1:
            ans.append(strs)
            return ans
        myMap = {}
        for each in strs:
            temp = sorted(each)
            check = "".join(temp)
            if check in myMap:
                myMap[check].append(each)
            else:
                myMap[check] = [each]
        for val in myMap.values():
            ans.append(val)
        return ans