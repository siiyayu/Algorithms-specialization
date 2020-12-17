# Uses python3
import sys
def lcs2(a, b):
    T = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        T[i][0] = 0
    for j in range(len(b) + 1):
        T[0][j]= 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                diff = 1
            else:
                diff = 0
            T[i][j] = max(T[i-1][j], T[i][j-1], T[i-1][j-1] + diff)
    return T[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    print(lcs2(a, b))

    # print(lcs2([2, 7, 8, 3], [5, 2, 8, 7]))
    # print(lcs2([7], [1, 2, 3, 4]))
    # print(lcs2([1, 2, 0, 4, 5, 6], [1, 2, 3, 4]))
    # print(compute_T_matrix([1, 3, 2, 3, 4], [4, 3, 4, 4]))
    # print(lcs2([1, 3, 2, 3, 4], [4, 3, 4, 4]))
