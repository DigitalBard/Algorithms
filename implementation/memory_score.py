def solution(name, yearning, photo):
    answer = []
    score = 0 # 추억 점수
    
    for p in photo: # 각 사진에 대하여
        for i, n in enumerate(name): # 그리워하는 사람의 이름과 인덱스 추출
            if n in p: # 해당 사진에 그리워하는 사람이 있으면
                score += yearning[i] # 인덱스에 해당하는 점수(yearning[i])를 더함
        answer.append(score) # 사진 하나에 대한 추억 점수 계산이 끝나면 결과 목록에 추가
        score = 0 # 추억 점수 초기화

    return answer # 결과 목록 반환