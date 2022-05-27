A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
count = [0] * 10
for x in str(A * B * C):
    count[int(x)] += 1
result_count = [str(a) for a in count]
print("\n".join(result_count))