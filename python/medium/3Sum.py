class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_zeros = nums.count(0)
        nums.append(0)
        nums.sort()
        first_positive = nums.index(0)
        nums.remove(0)
        positive_set = set(nums[first_positive:])
        negative_set = set(nums[:first_positive])

        results = set()
        if n_zeros > 0:
            if n_zeros >= 3:
                results.add((0, 0, 0))
            for num in nums:
                if num < 0 and -num in positive_set:
                    results.add((num, 0, -num))
                if num > 0 and -num in negative_set:
                    results.add((-num, 0, num))

        for left_idx, left in enumerate(nums[:first_positive - 1]):
            for right in nums[left_idx + 1:first_positive]:
                target = -(left + right)
                if target in positive_set:
                    results.add((left, right, target))

        for left_idx, left in enumerate(nums[first_positive:]):
            for right in nums[first_positive + left_idx + 1:]:
                target = -(left + right)
                if target in negative_set:
                    results.add((target, left, right))

        return results
