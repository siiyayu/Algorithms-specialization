# Uses python3
from math import inf


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(i, j, m, M, ops):
    minimum = +inf
    maximum = -inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(M[i][k], M[k + 1][j], ops[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def get_maximum_value(digits, ops):
    #write your code here
    n = len(digits)
    m = [[0]*n for _ in range(0, n)]
    M = [[0]*n for _ in range(0, n)]
    for i in range(0, n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, ops)
    return M[0][n-1]


if __name__ == "__main__":
    dataset = input()
    # dataset = '1+5'
    # dataset = '5-8+7*4-8+9'
    digits = list(map(int, dataset[::2]))
    ops = list(dataset[1::2])
    print(get_maximum_value(digits, ops))
