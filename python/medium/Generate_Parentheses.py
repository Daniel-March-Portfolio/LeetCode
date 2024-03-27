class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = self.getParenthesis([], 0, 0, n)
        return ["".join(parenthes) for parenthes in parenthesis]

    def getParenthesis(self, previous: List[str], opened: int, closed: int, n: int) -> List[List[str]]:
        if opened == n and closed == n:
            return [previous]

        result = []
        if opened < n:
            result.extend(self.getParenthesis(previous + ["("], opened + 1, closed, n))
        if closed < opened:
            result.extend(self.getParenthesis(previous + [")"], opened, closed + 1, n))
        return result
