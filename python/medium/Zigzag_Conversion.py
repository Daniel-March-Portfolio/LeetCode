class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        direction = -1
        row = 0
        for idx, letter in enumerate(s):
            rows[row].append(letter)
            if idx % (numRows - 1) == 0:
                direction *= -1
            row += direction

        return "".join(["".join(row) for row in rows])