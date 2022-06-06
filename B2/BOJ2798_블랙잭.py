N, M = map(int, input().split())
card = [x for x in map(int, input().split())]
max_val = -1
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card_sum = card[i] + card[j] + card[k]
            if card_sum > max_val and card_sum <= M:
                max_val = card_sum
print(max_val)