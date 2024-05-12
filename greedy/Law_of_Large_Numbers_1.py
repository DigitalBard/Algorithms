# n, m, k를 공백으로 구분하여 입력 받기
n, m, k = map(int, input.split())

# n개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input.split()))

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

answer = 0

while True:
  for _ in range(k): # 가장 큰 수를 k번 더함
    if m == 0: # m이 0이라면 반복문 탈출
      break
    
    answer += first
    m -= 1 # 한 번 더할 때마다 1씩 빼기
  
  if m == 0: # m이 0이라면 반복문 탈출
    break
  
  answer += second # 두 번째로 큰 수 한 번 더하기
  m -= 1 # 한 번 더할 때마다 1씩 빼기
  
print(answer) # 최종 답안 출력