# n을 입력받기
n = int(input())

# n개의 정수를 입력받아 리스트에 저장
array = []
for _ in range(n):
  array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

for num in array:
  print(num, end=' ')