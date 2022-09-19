import math, sys
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node * 2, start, (start + end) // 2)
        init(a, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node * 2, start, (start + end) // 2, left, right)
    rsum = query(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)
    return lsum + rsum

def update_tree(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        update_tree(tree, node * 2, start, (start + end) // 2, index, diff)
        update_tree(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, diff)
        
def update(a, tree, n, index, val):
    diff = val - a[index]
    a[index] = val
    update_tree(tree, 1, 0, n-1, index, diff)
        
N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
tree = [0] * pow(2, math.ceil(math.log2(N)) + 1)
init(A, tree, 1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(A, tree, N, b - 1, c)
    else:
        print(query(tree, 1, 0, N - 1, b - 1, c - 1))