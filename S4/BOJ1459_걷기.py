X, Y, W, S = map(int, input().split())
print(min((X + Y) * W, (max(X, Y) - (X + Y) % 2) * S + ((X + Y) % 2) * W, min(X, Y) * S + (max(X, Y) - min(X, Y)) * W))