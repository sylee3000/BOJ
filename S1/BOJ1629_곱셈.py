A, B, C = map(int, input().split())

def multiple(x, y, z):
    if y == 1:
        return x % z
    elif y % 2 == 0:
        return (multiple(x, y // 2, z) ** 2) % z
    else:
        return ((multiple(x, y // 2, z) ** 2) * x) % z

print(multiple(A, B, C))