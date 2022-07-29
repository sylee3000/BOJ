N = int(input())
list = []
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        list.append(B)
if not list:
    print(-1)
else:
    print(min(list))