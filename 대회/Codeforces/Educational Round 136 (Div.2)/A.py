t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if (n == 2 and m == 3) or (n == 3 and m == 2) or (n == 3 and m == 3):
        print(2, 2)
    else:
        print(1, 1)