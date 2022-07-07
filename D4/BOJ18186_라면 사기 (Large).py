import sys
input = sys.stdin.readline

N, B, C = map(int, input().split())
ramen = list(map(int, input().split()))

total_cost = 0

if B <= C:
    total_cost = sum(ramen) * B
else:
    for i in range(N-2):
        if ramen[i+1] > ramen[i+2]:
            buy_2 = min(ramen[i], ramen[i+1] - ramen[i+2])
            ramen[i] -= buy_2
            ramen[i+1] -= buy_2
            total_cost += buy_2 * (B + C)
            
            buy_3 = min(ramen[i], ramen[i+1], ramen[i+2])
            ramen[i] -= buy_3
            ramen[i+1] -= buy_3
            ramen[i+2] -= buy_3
            total_cost += buy_3 * (B + 2 * C)
            
            total_cost += ramen[i] * B
            ramen[i] = 0
        else:
            buy_3 = min(ramen[i], ramen[i+1], ramen[i+2])
            ramen[i] -= buy_3
            ramen[i+1] -= buy_3
            ramen[i+2] -= buy_3
            total_cost += buy_3 * (B + 2 * C)
            
            total_cost += ramen[i] * B
            ramen[i] = 0
            
    remain_buy_2 = min(ramen[N-2], ramen[N-1])
    total_cost += remain_buy_2 * (B + C)
    ramen[N-2] -= remain_buy_2
    ramen[N-1] -= remain_buy_2

    total_cost += max(ramen[N-2], ramen[N-1]) * B

print(total_cost)