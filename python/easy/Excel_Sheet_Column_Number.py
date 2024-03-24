from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0

        for idx, column in enumerate(columnTitle):
            number *= 26
            number += ascii_uppercase.index(column) + 1

        return number