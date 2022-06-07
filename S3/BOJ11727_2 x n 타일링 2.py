n = int(input())
tiling = [0,1,3]
if n > 2:
    for i in range(3, n + 1):
        tiling.append(2 * tiling[i-2]+tiling[i-1])
print(tiling[n] % 10007)