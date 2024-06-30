from collections import Counter

def solution(X, Y):
    answer = ''
    count_X = Counter(X)
    count_Y = Counter(Y)
    for i in range(9, -1, -1):
        common = min(count_X[str(i)], count_Y[str(i)])
        if common == 0:
            continue
        else:
            answer += str(i) * common
            
    if answer == '':
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    
    return answer