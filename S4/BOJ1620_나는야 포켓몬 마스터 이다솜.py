N, M = map(int, input().split())
dict = {}
dict_reverse = {}
for i in range(1, N + 1):
    poke = input()
    dict[i] = poke
    dict_reverse[poke] = i
for _ in range(M):
    q = input()
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict_reverse[q])
## pypy3으로 제출