T = int(input())
ans = ''
while T > 0:
    T, k = T // 9, T % 9
    ans += str(k)
print(ans[::-1])