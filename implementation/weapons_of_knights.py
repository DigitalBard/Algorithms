import math

def count_aliquot(num):
    aliquot = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            aliquot.add(i)
            aliquot.add(num // i)
    
    return len(aliquot)

def solution(number, limit, power):
    answer = 1
    for i in range(2, number + 1):
        atk = count_aliquot(i)
        if atk > limit:
            atk = power
        answer += atk
        
    return answer