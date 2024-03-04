class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)

        left_i = 0
        right_i = len(nums) - 1

        while left_i < right_i:
            middle_i = (left_i + right_i) // 2

            if nums[middle_i] == target:
                return middle_i
            if nums[middle_i] < target:
                left_i = middle_i+1
            else:
                right_i = middle_i

        return left_i