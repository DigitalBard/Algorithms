# 최초 제출
def solution1(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
        
    for name in callings:
        players[rank[name] - 1], players[rank[name]] = players[rank[name]], players[rank[name] - 1]
        rank[players[rank[name]]] += 1
        rank[name] -= 1

    return players
  
# enumerate 활용
def solution2(players, callings):
    rank = {key: i for i, key in enumerate(players)}
        
    for name in callings:
        called = rank[name]
        players[called - 1], players[called] = players[called], players[called - 1]
        rank[players[called]] += 1
        rank[name] -= 1

    return players