A, B = input().split()
A_sum, B_sum = 0, 0
for i in range(len(A)):
    A_sum += int(A[i])
for i in range(len(B)):
    B_sum += int(B[i])
print(A_sum * B_sum)