K = int(input())
str = input()

res = 0
last_count = 0
cur_count = 0
last_word = ''
for i in str:
    if last_word == '':
        last_word = i
        cur_count += 1
    elif last_word == i:
        cur_count += 1
    else:
        res = max(res, min(last_count, cur_count))
        last_word = i
        last_count = cur_count
        cur_count = 1
res = max(res, min(last_count, cur_count))
print(res * 2)