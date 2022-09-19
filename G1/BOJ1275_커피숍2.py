import sys, math
input = sys.stdin.readline

def init(A, tree, node, start, end):
    if start == end:
        tree[node] = A[start]
    else:
        init(A, tree, node * 2, start, (start + end) // 2)
        init(A, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
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

def update(A, tree, n, index, value):
    diff = value - A[index]
    A[index] = value
    update_tree(tree, 1, 0, n-1, index, diff)
    
N, Q = map(int, input().split())
A = list(map(int, input().split()))

tree = [0] * pow(2, math.ceil(math.log2(N)) + 1)
init(A, tree, 1, 0, N-1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(query(tree, 1, 0, N-1, min(x, y)-1, max(x, y)-1))
    update(A, tree, N, a-1, b)