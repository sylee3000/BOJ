import math

A, B = map(int, input().split())

k = int(math.log2(B)) + 1
dp = [0, 1]
for i in range(2, k + 1):
    dp.append(2 ** (i - 1) + 2 * dp[i - 1])

def part_sum(x):
    if x <= 0:
        return 0
    elif x == pow(2, int(math.log2(x))):
        return dp[int(math.log2(x))] + 1
    else:
        return dp[int(math.log2(x))] + x - pow(2, int(math.log2(x))) + 1 + part_sum(x - pow(2, int(math.log2(x))))

print(part_sum(B) - part_sum(A - 1))