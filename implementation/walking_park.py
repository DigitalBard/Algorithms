def solution(park, routes):
    answer = []
    
    row, col = len(park), len(park[0])
    
    for y in range(row):
        if 'S' in park[y]:
            x = park[y].find('S')
            answer = [y, x]
            break
    
    dx = {'E': 1, 'W': -1, 'S': 0, 'N': 0}
    dy = {'E': 0, 'W': 0, 'S': 1, 'N': -1}
    
    for r in routes:
        direction, distance = r.split()
        distance = int(distance)
        
        rollback = answer
        for _ in range(distance):
            ny = answer[0] + dy[direction]
            nx = answer[1] + dx[direction]
            
            if 0 <= nx < col and 0 <= ny < row:
                if park[ny][nx] == 'X':
                    answer = rollback
                    break
                else:
                    answer = [ny, nx]
                    
            else:
                answer = rollback
                break
        
    return answer