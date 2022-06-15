X, K = map(int, input().split())
X_bin = bin(X)[2:]
K_bin = bin(K)[2:]

X_bin = X_bin[::-1]
K_bin = K_bin[::-1]

X_one_count = 0
X_index = len(X_bin) - 1
while X > 0: 
    if X >= 2 ** X_index:
        X_one_count += 1
        X = X - 2 ** X_index
    X_index -= 1

arr = [0] * max(len(X_bin), (X_one_count + len(K_bin)))

for i in range(len(X_bin)):
    arr[i] = int(X_bin[i])
    
k_arr = []
for i in range(len(arr)):
    if arr[i] == 0:
        k_arr.append(i)

result = 0
for i in range(len(K_bin)):
    result += int(K_bin[i]) * (2 ** k_arr[i])
print(result)