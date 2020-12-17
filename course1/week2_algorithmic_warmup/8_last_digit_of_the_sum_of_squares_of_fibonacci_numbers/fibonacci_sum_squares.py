# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def get_pesano(n, m):
    pesano = []
    pesano.append(0)
    if m == 1:
        return pesano
    pesano.append(1)
    n0 = 0
    n1 = 1
    for i in range(0, m * 6):
        n0, n1 = n1, (n1 + n0) % m
        pesano.append(n1 % m)
        if pesano[-1] == 1 and pesano[-2] == 0:
            break
    return pesano[:-2] #len = 62


def fibonacci_sum_squares_fast(n):
    if n <= 1:
        return n
    pesano = get_pesano(1000, 10)
    return pesano[n % len(pesano)] * pesano[(n+1) % len(pesano)] % 10

if __name__ == '__main__':
    n = int(stdin.read())
    # n = int(input())
    print(fibonacci_sum_squares_fast(n))
