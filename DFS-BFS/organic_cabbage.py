import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, m, n, farm):
  if x <= -1 or x >= m or y <= -1 or y >= n:
    return False
  if farm[y][x] == 1:
    farm[y][x] = 2
    dfs(x - 1, y, m, n, farm)
    dfs(x, y - 1, m, n, farm)
    dfs(x + 1, y, m, n, farm)
    dfs(x, y + 1, m, n, farm)
    return True
  return False

t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  farm = [[0] * m for _ in range(n)]

  for _ in range(k):
    x, y = map(int, input().split())
    farm[y][x] = 1

  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(j, i, m, n, farm):
          result += 1

  print(result)

