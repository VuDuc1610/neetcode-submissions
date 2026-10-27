class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for i in range(len(details)):
            ageStr = details[i][11:13]
            if int(ageStr) > 60:
                ans += 1
            
        return ans