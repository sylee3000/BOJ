n = int(input())
list = [x for x in range(1, n + 1)]
stack = []
target = []
for _ in range(n):
    target.append(int(input()))
target_num = target.pop(0)
result = []
is_err = False
stack.append(list.pop(0))
result.append('+')

while target or stack:
    if not stack:
        stack.append(list.pop(0))
        result.append('+')
    if stack[-1] == target_num:
        stack.pop()
        if target:
            target_num = target.pop(0)
        result.append('-')
    elif not list:
        print("NO")
        is_err = True
        break
    else:
        stack.append(list.pop(0))
        result.append('+')

if not is_err:
    for r in result:
        print(r)