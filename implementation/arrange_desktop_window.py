def solution(wallpaper):
    r, c = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = r, c, 0, 0
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
                
    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer
  
# 얼마 안 되니 모아놓고 한 번에 비교
def solution(wallpaper):
    x, y = [], []
    r, c = len(wallpaper), len(wallpaper[0])
    
    for i in range(r):
      for j in range(c):
        if wallpaper[i][j] == '#':
          x.append(i)
          y.append(j)
                
    answer = [min(x), min(y), max(x) + 1, max(y) + 1]
    return answer