N, r, c = map(int, input().split())

def Z(x, y, r, c, n):
    if n == 1:
        return (r-x) * 2 + (c-y)
    else:
        part = 0
        next_x = x
        next_y = y
        if r >= x + (2 ** (n-1)):
            next_x = x + (2 ** (n-1))
            part += 2
        if c >= y + (2 ** (n-1)):
            next_y = y + (2 ** (n-1))
            part += 1
        return part * ((2 ** (n-1)) ** 2) + Z(next_x, next_y, r, c, n-1)
print(Z(0, 0, r, c, N))