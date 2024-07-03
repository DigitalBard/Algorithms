def solution(sizes):
    answer = [sizes[0][0], sizes[0][1]]
    long = max(answer)
    short = min(answer)
    for i in range(1, len(sizes)):
        big = max(sizes[i][0], sizes[i][1])
        small = min(sizes[i][0], sizes[i][1])
        if big > long and small <= short:
            answer = [big, short]
        elif big > long and small > short:
            answer = [big, small]
        elif big <= long and small > short:
            answer = [long, small]
        
        long = max(answer)
        short = min(answer)
        print(answer)
    return answer[0] * answer[1]

# 회전시킨다는 것은 높이와 너비 값을 바꾼다는 것
def solution(sizes):
    width = 0
    height = 0
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
        
        width = max(width, w)
        height = max(height, h)
        
    return width * height