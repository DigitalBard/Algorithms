# 1. min() 함수를 사용하는 방법

# n, m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0

# 한 줄의 입력받아 확인
for _ in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)
  
print(result)

# 2. 이중 반복문 구조를 이용한 방법

# n, m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력 받아 확인
for _ in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)
  
print(result)