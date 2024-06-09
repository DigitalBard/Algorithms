def solution(k, score):
    answer = []
    rank = []
    for s in score:
        if len(rank) < k:
            rank.append(s)
            rank.sort(reverse=True)
            answer.append(rank[-1])
        else:
            rank.append(s)
            rank.sort(reverse=True)
            rank.pop()
            answer.append(rank[-1])
    
    return answer
  
# min 함수가 있으므로 내가 일부러 정렬 안해도 됨
def solution(k, score):
    answer = []
    rank = []
    for s in score:
        rank.append(s)
        if len(rank) > k:
            rank.remove(min(rank))
        
        answer.append(min(rank))
    
    return answer