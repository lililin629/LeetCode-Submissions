class Solution:
    def reverseBits(self, n: int) -> int:
        # 00000010100101000001111010011100
        # 00111001011110000010100101000000
        ret = 0
        
        for i in range(32):
            digit = (n >> i) & 1
            ret |= (digit << (31-i))
        return ret