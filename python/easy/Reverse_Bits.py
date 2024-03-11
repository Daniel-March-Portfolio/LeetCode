class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        reversed_bits = bits[::-1] + "0"*(32 - len(bits))
        return int(reversed_bits, base=2)