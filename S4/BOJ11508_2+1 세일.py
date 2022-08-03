N = int(input())
cost = []
for _ in range(N):
    cost.append(int(input()))

cost.sort()
min_cost = 0

while len(cost) >= 3:
    for _ in range(2):
        min_cost += cost.pop()
    cost.pop()
min_cost += sum(cost)
print(min_cost)