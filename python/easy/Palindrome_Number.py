import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        lower_index = 0
        high_index = self._get_high_index(x)

        while lower_index < high_index:
            digit_1 = self._get_digit_form_number_by_index_starting_from_end(x, lower_index)
            digit_2 = self._get_digit_form_number_by_index_starting_from_end(x, high_index)
            if digit_1 != digit_2:
                return False

            lower_index += 1
            high_index -= 1
        return True

    def _get_digit_form_number_by_index_starting_from_end(self, num: int, index: int) -> int:
        return (num // (10**index)) % 10

    def _get_high_index(self, x: int) -> int:
        return int(math.log10(x))