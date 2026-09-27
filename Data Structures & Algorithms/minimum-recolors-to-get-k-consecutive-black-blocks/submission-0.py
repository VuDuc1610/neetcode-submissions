class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans, window = float('inf'),0

        for i in range(len(blocks)):
            if blocks[i] == "W":
                window += 1
            if i >= k and blocks[i-k] == "W":
                window -= 1
            if i >= k-1:
                ans = min(ans, window)
        return ans 