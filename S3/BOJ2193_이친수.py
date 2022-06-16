N = int(input())

pinary = [0, 1, 1, 2]

if N >= 4:
    for i in range(4, N + 1):
        pinary.append(pinary[i-2] + pinary[i-1])
print(pinary[N])