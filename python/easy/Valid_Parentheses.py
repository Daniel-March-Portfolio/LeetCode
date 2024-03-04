class Solution:
    opening = ["{", "(", "["]
    closing = ["}", ")", "]"]

    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in self.closing:
                if len(stack) == 0 or stack[-1] != self.opening[self.closing.index(i)]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
