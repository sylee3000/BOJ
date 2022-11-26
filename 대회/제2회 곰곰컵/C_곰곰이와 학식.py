A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

total = 0

if A >= X: # A 남음
    total += X
    A -= X
    if B >= Y: # B 남음
        total += Y
        B -= Y
        if C >= Z: # C 남음
            total += Z
            C -= Z
        else: # C 완료 -> A로 넘어감
            total += C
            X = (Z - C) // 3
            if A >= X: # A 남음
                total += X
            else: # A 완료 -> B로 넘어감
                total += A
                Y = (X - A) // 3
                total += min(B, Y)
    else: # B 완료 -> C + B 남은것
        total += B
        Z += (Y - B) // 3
        if C >= Z: # C 남음
            total += Z
        else: # C 완료 -> A로 넘어감
            total += C
            X = (Z - C) // 3
            total += min(A, X)
else:
    total += A
    Y += (X - A) // 3
    if B >= Y:
        total += Y
    else:
        total += B
        Z += (Y - B) // 3
        total += min(C, Z)
print(total)