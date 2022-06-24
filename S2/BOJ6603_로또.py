lotto_list = []
def pick_lotto(lst, a, l):
    if len(lotto_list) == 6:
        print(*lotto_list)
        return
    else:
        for i in range(a, l):
            if lst[i] not in lotto_list:
                lotto_list.append(lst[i])
                pick_lotto(lst, i, l)
                lotto_list.pop()
        

while True:
    lotto = list(map(int, input().split()))
    k = lotto.pop(0)
    if k == 0:
        break
    else:
        pick_lotto(lotto, 0, len(lotto))
    print()