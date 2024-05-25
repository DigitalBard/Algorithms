def solution(n, m, section):
    answer = 0
    while section:
        answer += 1
        sec = section.pop(0)
        while section:
            next = section.pop(0)
            if next >= sec + m:
                section.insert(0, next)
                break
            
    return answer
  
# 헷갈리니까 그냥 deque 쓰자
# 그리고 deque도 리스트니까 그냥 index로 접근 가능
from collections import deque

def solution(n, m, section):
    answer = 0
    dq = deque(section)
    while dq:
        answer += 1
        sec = dq.popleft()
        while dq and dq[0] < sec + m:
            dq.popleft()
            
    return answer