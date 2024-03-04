class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int, a))
        b = list(map(int, b))

        if len(a) > len(b):
            a, b = b, a

        idx = 1
        buffer = 0
        while idx <= len(b):
            if idx <= len(a):
                b[-idx] += a[-idx]
            b[-idx] += buffer
            buffer = 0

            if b[-idx] > 1:
                buffer = 1
                b[-idx] -= 2
            idx += 1
        if buffer > 0:
            b.insert(0, 1)

        return "".join(map(str, b))