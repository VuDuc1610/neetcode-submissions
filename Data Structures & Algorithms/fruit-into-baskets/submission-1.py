class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, myMap, l = 0, {}, 0

        for i in range(len(fruits)):
            myMap[fruits[i]] = 1 + myMap.get(fruits[i], 0)
            while len(myMap) > 2:
                myMap[fruits[l]] -= 1
                if myMap[fruits[l]] == 0:
                    del myMap[fruits[l]]
                l += 1
            ans = max(ans, i-l+1)
        return ans