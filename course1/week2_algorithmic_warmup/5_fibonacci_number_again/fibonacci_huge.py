# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


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
    return pesano[:-2]


def get_fibonacci_huge_fast(n, m):
    pesano = get_pesano(n, m)
    return pesano[n % len(pesano)]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
