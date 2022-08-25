def solution(numbers):
    answer = []
    for i in numbers:
        a = int(i)
        if ((a+1) & a) == 0:
            answer.append((a + 1) + (a + 1) // 2 - 1)
        else:
            k = 1
            res = 0
            while a > 0:
                if a % 2 == 1:
                    res += k
                    a //= 2
                    k *= 2
                else:
                    res += ((a + 1) * k - (k // 2))
                    break
                
            answer.append(res)
    
    return answer

print(solution([2,3]))