def solution(babbling):
    answer = 0
    
    for word in babbling:
        for cap in ["aya", "ye", "woo", "ma"]:
            if cap * 2 not in word:
                word = word.replace(cap, " ") # 해당 발음이 빠졌을 때 연속된 발음으로 인식되지 않도록 공백을 넣어서 구분
        if len(word.strip()) == 0:
            answer += 1
    
    return answer