# https://leetcode.com/problems/implement-queue-using-stacks/

# class Stack():
#     def __init__(self):
#         self.arr = []
#     def push(self, x: int) -> None:
#         self.arr.append(x)
#     def pop(self) -> int:
#         if len(self.arr) > 0:
#             return self.arr.pop()
#     def __len__(self):
#         return len(self.arr)

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s2.append(x)

    def pop(self) -> int:
        if len(self.s1) == 0:
            while len(self.s2) != 0:
                self.s1.append(self.s2.pop())
        return self.s1.pop()

    def peek(self) -> int:
        if len(self.s1) == 0:
            while len(self.s2) != 0:
                self.s1.append(self.s2.pop())
        return self.s1[-1]

    def empty(self) -> bool:
        return not (len(self.s1) or len(self.s2))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()