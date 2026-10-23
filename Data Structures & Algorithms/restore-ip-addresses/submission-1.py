class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def helper(i, tmp):
            if len(tmp) == 4:
                if i == len(s):
                    string = ".".join(map(str, tmp))
                    ans.append(string)
                return
            
            for j in range(i, min(i + 3, len(s))):
                cur = s[i:j+1]
                if len(cur) > 1 and cur[0] == "0":
                    return
                if int(cur) > 255:
                    return
                
                tmp.append(cur)
                helper(j+1, tmp)
                tmp.pop()
        
        helper(0, [])
        return ans

                
