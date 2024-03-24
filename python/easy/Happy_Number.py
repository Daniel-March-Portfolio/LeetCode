class Solution:
    def isHappy(self, n: int) -> bool:
        buffer = set()
        while n > 1:
            new_n = 0
            while n > 0:
                new_n += (n%10) ** 2
                n //= 10
            n = new_n
            if n in buffer:
                n = 0
            else:
                buffer.add(n)
        return bool(n)