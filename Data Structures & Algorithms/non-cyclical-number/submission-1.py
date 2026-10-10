class Solution:
    def isHappy(self, n: int) -> bool:
        def extract(n):
            ans = 0
            while n > 0:
                ans += (n % 10)*(n % 10)
                n = n // 10
            return ans
        
        hashSet = set()

        while True:
            if n == 1:
                return True
            else:
                n = extract(n)
                print(n)
                if n in hashSet:
                    return False
                hashSet.add(n)