def solution(s):
    answer = []
    memo = {}
    for i, c in enumerate(s):
        if c in memo:
            answer.append(i - memo[c])
            memo[c] = i
        else:
            answer.append(-1)
            memo[c] = i
            
    return answer