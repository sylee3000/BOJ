from collections import deque

N = int(input())
coin_value = deque(map(int, input().split()))

max_value = max(coin_value)
cost = 0
coin_count = 0
res = 0

while coin_value:
    part_cost = coin_value.popleft()
    if part_cost < max_value:
        cost += part_cost
        coin_count += 1
    else:
        res += max_value * coin_count - cost
        if coin_value:
            max_value = max(coin_value)
        cost = 0
        coin_count = 0
print(res)