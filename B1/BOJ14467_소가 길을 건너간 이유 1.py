cow = {}

cross_road = 0

N = int(input())
for _ in range(N):
    num, pos = map(int, input().split())
    if num not in cow.keys():
        cow[num] = pos
    else:
        if cow[num] != pos:
            cow[num] = pos
            cross_road += 1
            
print(cross_road)