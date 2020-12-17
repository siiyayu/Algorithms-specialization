# Uses python3
import sys

def optimal_weight(W, weights):
    # write your code here
    value = [[0]*(W + 1) for _ in range(0, len(weights) + 1)]
    for i in range(1, len(weights)+1):
        weights_idx = i - 1
        for w in range(1, W + 1):
            value[i][w] = value[i-1][w]
            if weights[weights_idx] <= w:
                val = value[i-1][w-weights[weights_idx]] + weights[weights_idx]
                if value[i][w] < val:
                    value[i][w] = val
    return value[len(weights)][W]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    # print(optimal_weight(10, [1, 4, 8]))
