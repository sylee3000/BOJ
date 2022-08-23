N = int(input())
F = int(input())
print(f'{(F - ((N // 100) * 100) % F) % F:0>2}')