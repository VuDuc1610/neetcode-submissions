class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = list(tiles)
        tiles.sort()
        ans = 0

        def helper(tiles, temp):
            nonlocal ans
            if not tiles:
                ans += 1
                return
            ans += 1
            for i in range(len(tiles)):
                if i > 0 and tiles[i] == tiles[i-1]:
                    continue
                helper(tiles[:i] + tiles[i+1:], temp)
                
        helper(tiles, [])
        return ans-1
                

