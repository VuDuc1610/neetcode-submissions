class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}
        ans,l,maxFreq = 0,0,0
        for i in range(len(s)):
            myMap[s[i]] = 1 + myMap.get(s[i],0)
            maxFreq = max(maxFreq, myMap[s[i]])
            while (i-l+1) - maxFreq > k:
                myMap[s[l]] -= 1
                l +=1
            ans = max(ans, i-l+1)
        return ans