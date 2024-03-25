from collections import deque


class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.len = 0

    def push(self, x: int) -> None:
        reversed_stack = deque()
        new_len = self.len + 1

        while self.len > 0:
            self.len -= 1
            reversed_stack.append(self.stack.pop())
        reversed_stack.append(x)
        while self.len < new_len:
            self.len += 1
            self.stack.append(reversed_stack.pop())

    def pop(self) -> int:
        self.len -= 1
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.len == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()