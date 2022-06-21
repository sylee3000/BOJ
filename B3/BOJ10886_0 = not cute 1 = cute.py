N = int(input())
op = {0:0, 1:0}
for _ in range(N):
    k = int(input())
    op[k] += 1
if op[0] > op[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')