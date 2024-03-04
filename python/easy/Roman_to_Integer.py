from typing import Iterator


class Solution:
    translator = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        return sum(self._romain_number_to_int_digits_generator(s))

    def _romain_number_to_int_digits_generator(self, number: str) -> Iterator[int]:
        idx = 0
        len_number = len(number)

        while idx < len_number - 1:
            first_num = self.translator[number[idx]]
            second_num = self.translator[number[idx + 1]]
            if first_num < second_num:
                yield second_num - first_num
                idx += 2
            else:
                yield first_num
                idx += 1
        if idx < len_number:
            yield self.translator[number[-1]]
