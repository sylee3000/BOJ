N = int(input())
res = 0
for _ in range(N):
    st, apple = map(int, input().split())
    res += apple % st
print(res)