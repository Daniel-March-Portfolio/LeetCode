class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = [1, 1]
        for i in range(rowIndex):
            middle = []
            for j in range(1, i + 1):
                middle.append(sum(row[j - 1: j + 1]))
            row = [1] + middle + [1]
        return row
