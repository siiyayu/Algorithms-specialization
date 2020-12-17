# Uses python3
import sys
import random
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

def partition3(a, l, r):
    m = partition2(a, l, r)
    x = a[m]
    j = m
    for i in range(m-1, l - 1, -1):
        if a[i] == x:
            j -= 1
            a[i], a[j] = a[j], a[i]
    return j, m

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1-1)
    randomized_quick_sort(a, m2+1, r)
    return

def intervals_counter(a, points):
    k = 0
    counts = {}
    for point in points:
        counts[point] = 0
    for i in range(0, len(a)):
        if a[i][1] == LEFT:
            k += 1
        if a[i][1] == RIGHT:
            k -= 1
        if a[i][1] == POINT:
            counts[a[i][0]] = k
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
    counts = optimal_points(starts, ends, points)
    # counts = optimal_points([1, 2, 3, 4], [5, 5, 5, 5], [2, 3, 5, 5])
    # points = [2, 3, 5, 5]
    for point in points:
        print(counts[point], end=' ')
# 2 3
# 0 5
# 7 10
# 1 6 11



