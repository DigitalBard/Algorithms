# n, m, k를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k + m % (k + 1)

answer = 0
answer += count * first # 가장 큰 수 더하기
answer += (m - count) * second # 두 번째로 큰 수 더하기

print(answer)