N = int(input())
max_price = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    price = 0
    if a == b == c:
        price = 10000 + a * 1000
    elif a == b or a == c:
        price = 1000 + a * 100
    elif b == c:
        price = 1000 + b * 100
    else:
        price = 100 * max(a, b, c)
    max_price = max(max_price, price)
print(max_price)