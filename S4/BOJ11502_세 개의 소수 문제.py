is_prime = [True] * 1001
prime = []

for i in range(2, 1001):
    if is_prime[i]:
        prime.append(i)
        for j in range(2 * i, 1001, i):
            is_prime[j] = False   

def find_three_prime(K):
    for a in prime:
        for b in prime:
            for c in prime:
                if a + b + c == K:
                    print(a, b, c)
                    return
    else:
        print(0)

T = int(input())
for _ in range(T):
    K = int(input())
    find_three_prime(K)
    