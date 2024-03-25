from math import log10

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1

        x *= sign
        result = 0

        n_digits = int(log10(x))
        while n_digits >= 0:
            result += x % 10 * (10**n_digits)
            n_digits -= 1
            x //= 10
        if result > 2**31 - 1:
            return 0
        return result * sign