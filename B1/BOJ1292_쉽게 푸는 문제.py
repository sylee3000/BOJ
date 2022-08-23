A, B = map(int, input().split())
num = 1
index = 1
cnt = 1
res = 0

while index <= B:
    if index >= A:
        res += num

    if cnt == num:
        num += 1
        cnt = 1
    else:
        cnt += 1
    index += 1
print(res)