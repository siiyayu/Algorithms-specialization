# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    total_cost = 0
    arr = [[value/weight, value, weight] for value, weight in zip(values, weights)]
    arr.sort(reverse=True)
    # write your code here
    for i in range(0, len(arr)):
        if capacity == 0:
            return total_cost
        if capacity < arr[i][2]:
            return capacity*arr[i][0] + total_cost
        total_cost += arr[i][1]
        capacity -= arr[i][2]
    return total_cost


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))

