L, P = map(int, input().split())
total = L * P
article = list(map(int, input().split()))
for i in range(5):
    print(article[i] - total, end = ' ')