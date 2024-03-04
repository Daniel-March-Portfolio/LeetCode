class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        min_int = 0
        max_int = x
        while min_int < max_int:
            mid_int = (max_int + min_int) // 2
            if mid_int * mid_int <= x:
                min_int = mid_int + 1
            else:
                max_int = mid_int
        return max_int - 1