import math

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

dist = (xs-xe) ** 2 + (ys-ye) ** 2
x, y = dx, dy
while y:
    x, y = y, x % y
else:
    gcd = x
dx, dy = dx // gcd, dy // gcd


while True:
    new_dist = (xs-(xe + dx)) ** 2 + (ys - (ye + dy)) ** 2
    if dist > new_dist:
        xe = xe + dx
        ye = ye + dy
        dist = new_dist
    else:
        print(xe, ye)
        break