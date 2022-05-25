N, K = map(int, input().split())
value_list = []
for i in range(N):
    value_list.append(int(input()))
    
coin_count = 0

for i in range(N):
    coin_value = value_list.pop()
    coin_count += K // coin_value
    K = K % coin_value
    if K == 0:
        break

print(coin_count)