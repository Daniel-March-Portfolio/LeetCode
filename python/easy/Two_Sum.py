class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left_i = 0
        right_i = len(nums) - 1

        while left_i < right_i:
            current_sum = sorted_nums[left_i] + sorted_nums[right_i]

            if current_sum == target:
                break
            if current_sum > target:
                right_i -= 1
            else:
                left_i += 1

        result = [None, None]
        for i, num in enumerate(nums):
            if num == sorted_nums[left_i] and result[0] is None:
                result[0] = i
            elif num == sorted_nums[right_i]:
                result[1] = i
        return result