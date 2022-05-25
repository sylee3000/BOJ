N = int(input())
min_count = 0
while N % 5 != 0:
    if N < 0:
        min_count = -1
        break
    else:
        min_count += 1
        N -= 3
if N > 0:
    min_count += N // 5
print(min_count)