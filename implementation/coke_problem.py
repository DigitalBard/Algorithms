def solution(a, b, n):
    answer = 0
    bottles = n
    while bottles >= a:
        new = bottles // a * b
        rest = bottles % a
        answer += new
        bottles = new + rest
    return answer