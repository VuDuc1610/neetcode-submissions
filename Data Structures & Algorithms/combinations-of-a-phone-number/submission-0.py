class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        if not digits:
            return ans

        def helper(tmp, idx):
            if len(tmp) == len(digits):
                ans.append(tmp)
                return
            
            for c in phone[digits[idx]]:
                helper(tmp + c, idx + 1)
        
        helper("", 0)

        return ans