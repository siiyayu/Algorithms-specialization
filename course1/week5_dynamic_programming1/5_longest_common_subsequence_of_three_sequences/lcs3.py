# Uses python3
import sys
import numpy as np


def lcs3(a, b, c):
    T = np.zeros((len(a) + 1, len(b) + 1, len(c) + 1), dtype=int)

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i-1] == b[j-1] == c[k-1]:
                    diff = 1
                else:
                    diff = 0
                T[i][j][k] = max(T[i-1][j][k],
                                 T[i][j-1][k],
                                 T[i][j][k-1],
                                 T[i-1][j-1][k],
                                 T[i-1][j][k-1],
                                 T[i][j-1][k-1],
                                 T[i-1][j-1][k-1] + diff,
                                 )
    return T[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
    # print(lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5]))
    # print(lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))



