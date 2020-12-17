#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []
        self.__max = -1
        self.__size = 0

    def Push(self, a):
        self.__stack.append(a)
        self.__size += 1
        if a >= self.__max:
            self.__max_stack.append(a)
            self.__max = a

    def Pop(self):
        assert self.__size != 0
        temp = self.__stack.pop()
        self.__size -= 1
        if temp == self.__max:
            self.__max_stack.pop()
            self.__max = self.__max_stack[-1]

    def Max(self):
        assert self.__size != 0
        return self.__max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
