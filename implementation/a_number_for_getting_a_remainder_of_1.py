import math

def solution(n):
    answer = n - 1
    for i in range(2, int(math.sqrt(n - 1)) + 1):
        if (n - 1) % i == 0:
            answer = i
            break
    return answer