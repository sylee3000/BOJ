x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
win = False

if x1 == x2:
    if x1 != x3:
        win = True
else:
    if x2 == x3:
        win = True
    else:
        if (y2 - y1) / (x2 - x1) != (y3 - y2) / (x3 - x2):
            win = True
if win:
    print("WINNER WINNER CHICKEN DINNER!")
else:
    print("WHERE IS MY CHICKEN?")