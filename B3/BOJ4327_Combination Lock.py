while True:
    start, one, two, three = map(int, input().split())
    if start == one == two == three == 0:
        break
    else:
        pos = start
        res = 1080
        if pos < one:
            res += 9 * (40 - (one - pos))
        else:
            res += 9 * (pos - one)
        pos = one
        
        if pos > two:
            res += 9 * (40 - (pos - two))
        else:
            res += 9 * (two - pos)
        pos = two
        
        if pos < three:
            res += 9 * (40 - (three - pos))
        else:
            res += 9 * (pos - three)
        print(res)