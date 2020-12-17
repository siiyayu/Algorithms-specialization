# Uses python3
import sys

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


def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n
    pesano = get_pesano(1000, 10)
    dev1 = m // len(pesano)
    dev2 = n // len(pesano)
    rem1 = m % len(pesano)
    rem2 = n % len(pesano)
    if (dev1 == dev2):
        return sum(pesano[rem1:rem2+1]) % 10
    return (sum(pesano) * (dev2 - dev1) + (sum(pesano[rem1:]) + sum(pesano[rem1:])) )%10


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))