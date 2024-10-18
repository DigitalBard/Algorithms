n = int(input())

units = [3, 5]

dp = [5001] * (n+1)
dp[0] = 0

for i in range(3, n+1):
  for j in units:
    if dp[i-j] != 5001:
      dp[i] = min(dp[i], dp[i-j] + 1)

if dp[n] == 5001:
  print(-1)
else:
  print(dp[n])