def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97, 123)]
    for ch in skip:
        alphabet.remove(ch)
    for ch in s:
        idx = (alphabet.index(ch) + index) % len(alphabet)
        answer += alphabet[idx]
            
    return answer