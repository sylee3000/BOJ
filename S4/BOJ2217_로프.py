N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope = sorted(rope)
max_weight = 0
for i in range(N, 0, -1):
    if max_weight < i * rope[N-i]:
        max_weight = i * rope[N-i]
print(max_weight)