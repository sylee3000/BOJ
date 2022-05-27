A, B = input().split()
rev_A = int(A[2::-1])
rev_B = int(B[2::-1])
print(max(rev_A, rev_B))