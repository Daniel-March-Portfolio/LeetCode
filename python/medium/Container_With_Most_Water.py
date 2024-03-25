class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_value = 0

        while left < right:
            value = min(height[left], height[right]) * (right - left)
            if value > max_value:
                max_value = value
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_value