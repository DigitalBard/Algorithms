def solution(k, m, score):
    answer = 0
    apples = len(score)
    
    if apples < m:
        return 0
    
    score.sort()
    for _ in range(apples // m):
        box = []
        for _ in range(m):
            box.append(score.pop())
        answer += min(box) * m
        
    return answer
  
# 정렬을 했으므로 m의 배수마다 최솟값이 나옴
def solution(k, m, score):
    answer = 0
    
    score.sort()
    answer = sum(score[len(score) % m::m] * m)
        
    return answer