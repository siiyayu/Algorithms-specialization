# Uses python3

import sys

def multiply_max(a, b):
    x1 = max(a)
    x2 = max(b)
    a.remove(x1)
    b.remove(x2)
    return x1*x2, a, b


def max_dot_product(a, b):
    # write your code here
    res = 0
    n = len(a)
    for _ in range(0, n):
        x, a, b = multiply_max(a, b)
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

