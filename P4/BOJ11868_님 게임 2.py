N = int(input())
stone_list = map(int, input().split())

xor_val = 0
for stone in stone_list:
    xor_val = xor_val ^ stone
    
if N == 1:
    print("koosaga")
else:
    if xor_val > 0:
        print("koosaga")
    else:
        print("cubelover")