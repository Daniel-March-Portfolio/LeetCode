class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])

        for left_idx in range(len(nums) - 2):
            for right_idx in range(left_idx + 2, len(nums)):
                required_middle = target - (nums[left_idx] + nums[right_idx])
                middle_idx = self.find_target_or_left_closest(nums, left_idx + 1, right_idx - 1, required_middle)
                closest = self.calc_closest(nums, left_idx, middle_idx, right_idx, target, closest)
        return closest

    def find_target_or_left_closest(self, nums: List[int], left: int, right: int, target: int) -> int:
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right

        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle - 1
        return left

    def calc_closest(self, nums: List[int], left_idx: int, middle_idx: int, right_idx: int, target: int, closest: int):
        middle_3sum = nums[left_idx] + nums[right_idx] + nums[middle_idx]
        if abs(middle_3sum - target) < abs(closest - target):
            closest = middle_3sum
        if middle_idx > left_idx + 1:
            middle_3sum = nums[left_idx] + nums[right_idx] + nums[middle_idx - 1]
            if abs(middle_3sum - target) < abs(closest - target):
                closest = middle_3sum
        if middle_idx < right_idx - 1:
            middle_3sum = nums[left_idx] + nums[right_idx] + nums[middle_idx + 1]
            if abs(middle_3sum - target) < abs(closest - target):
                closest = middle_3sum
        return closest