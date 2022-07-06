import sys
input = sys.stdin.readline

N = int(input())
edge = []
for _ in range(N-1):
    a, b = map(int, input().split())
    edge.append((a,b))

vertex = [1]
parent = [0] * (N + 1)
    
while edge:
    v = vertex.pop()
    for i in edge:
        if v in i:
            if i[0] == v:
                vertex.append(i[0])
                parent[i[1]] = v
            else:
                vertex.append(i[1])
                parent[i[0]] = v
            edge.remove(i)
print(*parent[2:])