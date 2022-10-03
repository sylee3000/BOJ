import math

n, m = map(int, input().split())
upper_2, lower_2, upper_5, lower_5 = 0, 0, 0, 0
k, l = 2, 5
while k <= n:
    upper_2 += (n // k) - math.ceil((n - m + 1) / k) + 1
    lower_2 += m // k
    k *= 2

while l <= n:
    upper_5 += (n // l) - math.ceil((n - m + 1) / l) + 1
    lower_5 += m // l
    l *= 5

print(min(upper_2 - lower_2, upper_5 - lower_5))