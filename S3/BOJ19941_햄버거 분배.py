N, K = map(int, input().split())
hamburger = [False] * N
person = []
h_and_p = input()

for i in range(N):
    if h_and_p[i] == 'H':
        hamburger[i] = True
    else:
        person.append(i)
        
max_hamburger = 0
for i in person:
    for j in range(i-K, i+K+1):
        if 0 <= j < N and hamburger[j] == True:
            max_hamburger += 1
            hamburger[j] = False
            break
print(max_hamburger)