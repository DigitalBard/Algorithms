def solution(keymap, targets):
    answer = []
    keydic = []
    for i, e in enumerate(keymap):
        keydic.append({})
        for j, c in enumerate(e):
            if c not in keydic[i].keys():
                keydic[i][c] = j + 1
            
    for target in targets:
        total = []
        for c in target:
            count = []
            for e in keydic:
                try:
                    k = e[c]
                    count.append(k)
                except:
                    pass
            
            if len(count) > 0:
                total.append(min(count))
            else:
                total.append(-1)
                break
        
        if -1 in total:
            answer.append(-1)
        else:
            answer.append(sum(total))
            
    return answer
  
  
## dictionary에 저장할 때 각 문자 입력을 위해 누르는 횟수를 최솟값으로 저장하면 더 간략화됨.
def solution(keymap, targets):
    answer = []
    keydic = {}
    for keypad in keymap:
        for i, c in enumerate(keypad):
            if c in keydic:
                keydic[c] = min(i + 1, keydic[c])
            else:
                keydic[c] = i + 1
    
    for target in targets:
        count = 0
        for c in target:
            if c not in keydic:
                count = -1
                break
            
            count += keydic[c]
        
        answer.append(count)
            
    return answer