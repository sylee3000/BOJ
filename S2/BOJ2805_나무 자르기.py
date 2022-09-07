N, M = map(int, input().split())
tree = list(map(int, input().split()))

mn, mx = 0, max(tree)
res = 0

while mn <= mx:
    center = (mn + mx) // 2
    tree_cut = 0
    for i in tree:
        if i > center:
            tree_cut += i - center
    if tree_cut >= M:
        res = max(res, center)
        mn = center + 1
    else:
        mx = center - 1
print(res)