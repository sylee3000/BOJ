N = int(input())
list = [x for x in map(int, input().split())]
count = 0
while list:
    num = list.pop()
    if num == 1:
        continue
    c = 1
    for i in range(num-1, 1, -1):
        if num % i == 0:
            c = 0
            break
    count += c
    
print(count)