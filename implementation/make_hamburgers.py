from collections import deque

def solution(ingredient):
    answer = 0
    stack = ''
    dq = deque(ingredient)
    while dq:
        i = dq.popleft()
        stack += str(i)
        if i == 1:
            if stack[-1:-5:-1] == '1321':
                stack = stack[:len(stack) - 4]
                answer += 1
    
    return answer
  
# 더 간단히
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if i == 1 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
              stack.pop()
    
    return answer