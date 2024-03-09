class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1,1]]
        for i in range(1, numRows):
            middle = []
            for j in range(1, i+1):
                middle.append( sum(result[-1][j-1: j+1]) )
            result.append([1] + middle + [1])
        return result[:numRows]