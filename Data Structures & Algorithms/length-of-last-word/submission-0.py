class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s)-1
        while s[index] == " ":
            index -= 1
        for i in range(index, -1, -1):
            if s[i] != " ":
                count += 1
            else:
                break
        return count