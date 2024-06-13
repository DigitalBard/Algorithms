n, k = map(int, input().split())
result = 0

# # n이 k 이상이면 k로 계속 나누기
# while n >= k:
#   # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
#   while n % k != 0:
#     n -= 1
#     result += 1
#   # k로 나누기
#   n //= k
#   result += 1
  
# while n > 1:
#   n -= 1
#   result += 1
  
# print(result)

# 1씩 빼지 않고 n이 k의 배수가 되도록 한번에 빼기
while True:
  # target = (n // k) * k
  # result += (n - target)
  # n = target
  
  if n < k:
    break
  
  n -= n % k
  result += n % k
  
  # if n < k:
  #   break
  
  n //= k
  result += 1
  
# 마지막으로 남은 수에 대해 1씩 빼기
result += (n - 1)

print(result)