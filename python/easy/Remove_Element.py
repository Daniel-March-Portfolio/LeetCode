class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        last_el_idx = len(nums) - 1
        while last_el_idx >= 0:
            if nums[last_el_idx] == val:
                del nums[last_el_idx]
            else:
                n += 1
            last_el_idx -= 1
        return n