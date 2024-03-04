class Solution:
    def climbStairs(self, n: int) -> int:
        buffer = {
            1: 1,
            2: 2
        }
        return self.climb_stairs(n, buffer)

    def climb_stairs(self, n: int, buffer: dict[int: int]) -> int:
        if n not in buffer:
            buffer[n] = self.climb_stairs(n - 1, buffer) + self.climb_stairs(n - 2, buffer)
        return buffer[n]

