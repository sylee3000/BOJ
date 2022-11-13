S = input()
T = input()

res = 0

def change(K, T):
    global res
    if K == T:
        res = 1
    elif K in T or K in T[::-1]:
        K1 = K + 'A'
        K2 = 'B' + K[::-1]
        change(K1, T)
        change(K2, T)
    else:
        return

change(S, T)
print(res)