from collections import Counter

N = int(input())
seat = Counter(input())

if seat["L"] > 0:
    print(seat["S"] + (seat["L"] // 2) + 1)
else:
    print(seat["S"])