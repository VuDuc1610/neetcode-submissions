class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ptr,ans,mySet = 0,0,set()
        mySet.add(s[0])
        for i in range(1,len(s)):
            while s[i] in mySet:
                mySet.remove(s[ptr])
                ptr += 1
            mySet.add(s[i])
            ans = max(ans,i-ptr+1)
        return ans
            