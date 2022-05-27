N = int(input())
time = [int(x) for x in input().split()]
time = sorted(time)
total_time = 0
while time:
    total_time += N * time.pop(0)
    N -= 1
print(total_time)