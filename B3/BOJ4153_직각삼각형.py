while True:
    triangle = sorted(list(map(int, input().split())))
    if triangle.count(0) == 3:
        break
    if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
        print("right")
    else:
        print("wrong")