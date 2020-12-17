# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops.insert(0, 0)
    stops.append(distance)
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and (stops[currentRefill + 1] - stops[lastRefill]) <= tank:
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills = numRefills + 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    # print(compute_min_refills(10, 3, [1, 2, 5, 9]))


