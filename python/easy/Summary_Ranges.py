class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []

        start = 0
        i=0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if i-1 == start:
                    result.append(f"{nums[start]}")
                else:
                    result.append(f"{nums[start]}->{nums[i-1]}")
                start = i
        if i == start:
            result.append(f"{nums[start]}")
        else:
            result.append(f"{nums[start]}->{nums[i]}")
        return result