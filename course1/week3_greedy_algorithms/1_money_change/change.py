# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10, 5, 1]
    n1 = m // 10
    n2 = (m - 10*n1) // 5
    n3 = m - n1*10 - n2*5
    return n1 + n2 + n3

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
