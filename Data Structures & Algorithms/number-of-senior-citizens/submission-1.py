class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for detail in details:
            ageStr = detail[11:13]
            if int(ageStr) > 60:
                ans += 1
            
        return ans