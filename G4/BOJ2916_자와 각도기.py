N, K = map(int, input().split())
CY = list(map(int, input().split()))
HW = list(map(int, input().split()))

available = []

for i in CY:
    k = i
    while True:
        k += i
        if k >= 360:
            k -= 360
        if k == i:
            break
        else:
            available.append(k)
            
for i in HW:
    if i in available:
        print("YES")
    else:
        print("NO")
