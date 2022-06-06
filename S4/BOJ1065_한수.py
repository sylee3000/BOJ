N = int(input())

def d(N):
    count = 0
    for i in range(1, N+1):
        if i<100:
            count += 1
        else:
            digit_100 = i // 100
            digit_10 = (i % 100) // 10
            digit_1 = i % 10
            if digit_100 - digit_10 == digit_10 - digit_1:
                count += 1
    return count
print(d(N))