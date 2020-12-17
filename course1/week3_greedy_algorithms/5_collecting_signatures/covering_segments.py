# Uses python3
import sys
from collections import namedtuple

LEFT = 1
POINT = 2
RIGHT = 3

def get_list_to_sort(starts, ends, points):
    result = []
    for i in range(0, len(starts)):
        result.append([starts[i], LEFT])
        result.append([ends[i], RIGHT])
    for i in range(0, len(points)):
        result.append([points[i], POINT])
    return result

def less_or_equal(x, y):
    return less(x, y) or equal(x, y)

def less(x, y):
    return (x[0] < y[0])\
           or (x[0] == y[0] and x[1] < y[1])

def equal(x, y):
    return x[0] == y[0] and x[1] == y[1]

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l+1, r+1):
        if less_or_equal(a[i], x):
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m-1)
    randomized_quick_sort(a, l, m+1)
    return

def intervals_counter(a, points):
    k = 0
    counts = []
    for i in range(0, len(a)):
        if a[1] == LEFT:
            k += 1
        if a[1] == RIGHT:
            k -= 1
        if a[1] == POINT:
            counts.append(k)
    return counts

def optimal_points(starts, ends, points):
    a = get_list_to_sort(starts, ends, points)
    randomized_quick_sort(a, 0, len(a) - 1)
    counts = intervals_counter(a, points)
    return counts

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    counts = fast_count_segments(starts, ends, points)
    for c in coints:
        print(c, end=' ')
