class Solution:
    def reverseBits(self, n: int) -> int:
        #get the rightmost bit from n
        #push result 1 bit to the left
      #add that bit into the result
        #remove the right most bit from n

        result = 0
        for _ in range(32):
            bit = n&1
            result <<= 1
            result += bit
            n>>=1
        return result