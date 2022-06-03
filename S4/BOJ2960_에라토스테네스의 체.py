from collections import deque

N, K = map(int, input().split())
d = deque([x for x in range(2, N+1)])
pop_list = []

while d:
    a = d.popleft()
    pop_list.append(a)
    for i in list(d):
        if i % a == 0:
            d.remove(i)
            pop_list.append(i)
    if len(pop_list) - 1 >= K:
        break
print(pop_list[K-1])