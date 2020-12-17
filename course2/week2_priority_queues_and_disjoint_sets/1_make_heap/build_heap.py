# python3


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


class HeapSort(object):

    def __init__(self, data):
        self.data = data
        self.size = self.get_size(data)
        self.swaps = []

    @classmethod
    def get_size(self, data):
        return len(data)

    def left_child(self, i):
        return 2 * (i + 1) - 1

    def right_child(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1 # !!!!!

    # def sift_down(self, i): #for max-heap
    #     max_index = i
    #     l = self.left_child(i)
    #     if l <= self.size - 1 and self.data[l] > self.data[max_index]:
    #         max_index = l
    #     r = self.right_child(i)
    #     if r <= self.size - 1 and self.data[r] > self.data[max_index]:
    #         max_index = r
    #     if i != max_index:
    #         self.swaps.append((i, max_index))
    #         self.data[i], self.data[max_index] = self.data[max_index], self.data[i]
    #         self.sift_down(max_index)

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= self.size - 1 and self.data[l] < self.data[min_index]:
            min_index = l
        r = self.right_child(i)
        if r <= self.size - 1 and self.data[r] < self.data[min_index]:
            min_index = r
        if i != min_index:
            self.swaps.append((i, min_index))
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.sift_down(min_index)

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down(i)

    def heap_sort(self):
        n = self.size
        self.build_heap()
        for i in range(n):
            self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
            self.size -= 1
            self.sift_down(0)
        return self.swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    c = HeapSort(data)
    # c = HeapSort([5, 4, 3, 2, 1])
    # c = HeapSort([1, 2, 3, 4, 5])
    c.build_heap()
    print(len(c.swaps))
    if len(c.swaps) > 0:
        for i, j in c.swaps:
            print(i, j)
    #
    # print(len(swaps))



if __name__ == "__main__":
    main()
