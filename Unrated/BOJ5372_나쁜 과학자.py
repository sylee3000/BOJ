import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    k = int(input())
    m = int(input())
    
    p = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        p[x].append(y)
        p[y].append(x)
    
    remove_count = 0
    
    while True:
        max_relevant = -1
        max_relevant_count = 0
        for i in range(1, n+1):
            if len(p[i]) > max_relevant_count:
                max_relevant = i
                max_relevant_count = len(p[i])
        if max_relevant_count == 0:
            break
        for i in p[max_relevant]:
            p[i].remove(max_relevant)
        p[max_relevant] = []
        remove_count += 1
    if remove_count <= k:
        print(remove_count)
    else:
        print("IMPOSSIBLE")