T = int(input())
for i in range(T):
    n = int(input())
    print('#'*n)
    for _ in range(n-2):
        print('#'+'J'*(n-2)+'#')
    if n != 1:
        print('#'*n)
    if i < T-1:
        print()