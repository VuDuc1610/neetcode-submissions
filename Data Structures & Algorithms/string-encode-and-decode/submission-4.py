class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            element = str(length) + "#" + s
            res += element
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            part = s.split('#', 1)
            length = int(part[0])
            res.append(part[1][:length])
            s = part[1][length:]
        return res
