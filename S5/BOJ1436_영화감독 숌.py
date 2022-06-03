N = int(input())
count = 1
series_number = 666
c = True
while c:
    if "666" in str(series_number):
        if count == N:
            print(series_number)
            c = False
        else:
            count += 1
    series_number += 1