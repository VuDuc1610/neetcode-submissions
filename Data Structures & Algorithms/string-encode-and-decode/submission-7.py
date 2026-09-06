class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for var in strs:
            length = len(var)
            temp = f"{length}#{var}"
            encoded_string += temp
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        while len(s) > 0:
            index = 0
            while s[index] != "#":
                index += 1
            length = int(s[0:index])
            tempStr = s[1+index:length+index+1]
            decoded_strs.append(tempStr)
            s = s[1+length+index:]
        return decoded_strs