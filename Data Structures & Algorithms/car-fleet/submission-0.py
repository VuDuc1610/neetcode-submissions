class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPos = sorted(position)
        stack = []
        ans = 0
        map = {}
        for i in range(len(speed)):
            map[position[i]] = speed[i]

        for i in range(len(sortedPos)-1, -1, -1):
            time = (target-sortedPos[i])/map[sortedPos[i]]
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        
        while stack:
            ans += 1
            stack.pop()
        return ans
