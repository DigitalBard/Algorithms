import sys 

n = int(sys.stdin.readline().rstrip()) 

scores = []
for k in range(n):
    d, i = map(int, sys.stdin.readline().rstrip().split())
    scores.append((d, i, k))

scores = sorted(scores, key=lambda x: (x[0], x[1]), reverse=True)

rank = list(range(1, n+1))
for j in range(n):
    for i in range(j+1, n):
        if (scores[j][1] < scores[i][1] or (scores[j][0] == scores[i][0] and scores[j][1] == scores[i][1])):
            if rank[i] > rank[j]:
                rank[i] = rank[j]
            elif rank[i] < rank[j]:
                rank[j] = rank[i]

result = [0] * n

for i in range(n):
    result[scores[i][2]] = rank[i]

for r in result:
    print(r, end=' ')