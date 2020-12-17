# python3

from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

def max_sliding_window_fast(sequence, m, n):
    d = deque()
    res = []
    for i in range(m):
        while d and sequence[i] >= sequence[d[-1]]:
            d.pop()
        d.append(i)
    for i in range(m, n):
        res.append(sequence[d[0]])
        while d and d[0] <= i - m:
            d.popleft()
        while d and sequence[i] >= sequence[d[-1]]:
            d.pop()
        d.append(i)
    res.append(sequence[d[0]])
    return res


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    # print(*max_sliding_window_fast([2, 7, 3, 1, 5, 2, 6, 2], 4, 8))
    print(*max_sliding_window_fast(input_sequence, window_size, n))
