class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.replace(" ", "")
        arr = re.sub(r'[^a-zA-Z0-9]', '', temp).lower()
        return arr == arr[::-1]