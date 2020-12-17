# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_fast(a, b):
	if b == 0:
		return a
	a = a % b
	return gcd_fast(b, a)

def lcm_fast(a, b):
	d = gcd_fast(a, b)
	return int(a*b/d)
	

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

