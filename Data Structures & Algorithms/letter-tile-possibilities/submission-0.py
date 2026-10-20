class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = list(tiles)
        tiles.sort()

        ans = []

        def helper(tiles, temp):
            if not tiles:
                ans.append(temp[:])
                return
            ans.append(temp[:])
            for i in range(len(tiles)):
                if i > 0 and tiles[i] == tiles[i-1]:
                    continue
                temp.append(tiles[i])
                helper(tiles[:i] + tiles[i+1:], temp)
                temp.pop()
        helper(tiles, [])
        return len(ans)-1
                
