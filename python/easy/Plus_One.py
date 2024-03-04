class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        idx = len(digits) - 1

        while idx > 0:
            if digits[idx] > 9:
                digits[idx - 1] += 1
                digits[idx] = digits[idx] - 10
            idx -= 1
        if digits[0] > 9:
            digits[0] -= 10
            digits.insert(0, 1)

        return digits
