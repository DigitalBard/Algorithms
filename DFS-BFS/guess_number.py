import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
max_limit = max(n, k) * 2

arr = [0] * (max_limit + 1)

dq = deque([k])

while dq:
    pos = dq.popleft()

    if pos == n:
        break

    next = [pos + 1, pos - 1, pos * 2]

    for num in next:
        if num >= 0 and num < max_limit and arr[num] == 0:
            arr[num] = arr[pos] + 1
            dq.append(num)

print(arr[n])