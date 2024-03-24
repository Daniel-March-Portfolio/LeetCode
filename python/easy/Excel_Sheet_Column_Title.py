class Solution:
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def convertToTitle(self, columnNumber: int) -> str:
        result_letters = []
        while columnNumber > 0:
            cur_column = (columnNumber - 1) % 26
            result_letters.append(self.upper_letters[cur_column])
            columnNumber = (columnNumber - 1) // 26

        return "".join(result_letters[::-1])