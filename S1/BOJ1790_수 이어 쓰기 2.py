N, k = map(int, input().split())

l = 1
    
while k > 0:
    if k > 9 * (10 ** (l - 1)) * l:
        k -= 9 * (10 ** (l - 1)) * l
        l += 1
    else:
        break
    
result_number = str(10 ** (l - 1) + ((k - 1) // l))
result_index = (k - 1) % l 

if int(result_number) > N:
    print(-1)
else:
    print(result_number[result_index])