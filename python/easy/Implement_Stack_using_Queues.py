class MyStack:

    def __init__(self):
        self.__list = []
        self.__len = 0

    def push(self, x: int) -> None:
        self.__list.append(x)
        self.__len += 1

    def pop(self) -> int:
        self.__len -= 1
        return self.__list.pop()

    def top(self) -> int:
        return self.__list[-1]

    def empty(self) -> bool:
        return self.__len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()