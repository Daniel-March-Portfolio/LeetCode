class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        buffer = set()
        for idx, num in enumerate(nums):
            if idx == k:
                break
            if num in buffer:
                return True
            buffer.add(num)

        for i in range(k, len(nums)):
            if nums[i] in buffer:
                return True
            buffer.add(nums[i])
            buffer.remove(nums[i-k])
        return False