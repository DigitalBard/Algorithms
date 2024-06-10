def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    
    rev = list(answer)
    rev.reverse()
    rev = ''.join(rev)
    answer += '0' + rev
    
    return answer
  
# 거꾸로 뒤집는 건 문자열 슬라이싱 이용해서도 가능
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    
    answer += '0' + answer[::-1]
    
    return answer