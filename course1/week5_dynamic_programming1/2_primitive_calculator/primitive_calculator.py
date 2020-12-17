# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    prev = []
    T = []
    T.append(0)
    prev.append(0)
    T.append(0)
    prev.append(0)
    if n == 1:
        return [1]
    for number in range(2, n+1):
        comp = {}
        indices = {}
        if number % 2 == 0:
            comp['dev2'] = T[number//2]
            indices['dev2'] = number//2
        if number % 3 == 0:
            comp['dev3'] = T[number//3]
            indices['dev3'] = number//3
        comp['minus1'] = T[number-1]
        indices['minus1'] = number-1
        minimum = min(comp, key=comp.get)
        T.append(T[indices[minimum]]+1) # array for minimum counts of operations, index = number
        prev.append(indices[minimum]) # array for numbers
    idx = n
    while idx > 0:
        sequence.append(idx)
        idx = prev[idx]
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
