class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr,ans,mySet = 0,0,set()

        for i in range(len(s)):
            while s[i] in mySet:
                mySet.remove(s[ptr])
                ptr += 1
            mySet.add(s[i])
            ans = max(ans,i-ptr+1)
        return ans
            