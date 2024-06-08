def solution(t, p):
    answer = 0
    length = len(t)
    interval = len(p)
    for i in range(length):
        left = i
        right = i + interval
        if right > length:
            break

        if int(t[left:right]) <= int(p):
            answer += 1


    return answer