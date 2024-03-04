class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        right_el_idx = n - 1

        while right_el_idx > 0:
            if nums[right_el_idx] == nums[right_el_idx - 1]:
                n -= 1
                del nums[right_el_idx]
            right_el_idx -= 1

        return n
