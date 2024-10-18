class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    total_cost = 0
    edges.sort(key=lambda x: x[2])  

    for a, b, cost in edges:
        if uf.find(a) != uf.find(b):  
            uf.union(a, b) 
            total_cost += cost

    return total_cost


n, m = map(int, input().split())  
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))  

result = kruskal(n, edges)
print(result)
