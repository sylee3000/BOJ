T = int(input())
for _ in range(T):
    str = input()
    count = 0
    for s in str:
        if s == "(":
            count += 1
        elif s == ")":
            count -= 1
        if count < 0:
            break
    if count != 0:
        print("NO")
    else:
        print("YES")