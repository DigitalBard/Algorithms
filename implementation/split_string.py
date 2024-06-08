from collections import deque

def solution(s):
    answer = 0
    dq = deque(s)
    first = dq[0]
    same = 0
    diff = 0
    
    while dq:
        nextCh = dq.popleft()
        if nextCh == first:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            if dq:
                first = dq[0]
        elif same != diff and len(dq) == 0:
            answer += 1
                
    return answer