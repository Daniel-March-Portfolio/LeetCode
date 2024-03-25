import re

class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = re.findall(r"^ *[-\+]?\d+", s)
        if len(numbers) == 0:
            return 0
        integer = int(numbers[0])
        return min(2**31-1,max(-2**31, integer))
