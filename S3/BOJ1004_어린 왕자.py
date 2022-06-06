import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planet = []
    result = 0
    for _ in range(n):
        planet.append(list(map(int, input().split())))
    for i in planet:
        x1_in_planet = 0
        x2_in_planet = 0
        if math.sqrt((x1-i[0]) ** 2 + (y1-i[1]) ** 2) < i[2]:
            x1_in_planet = 1
        if math.sqrt((x2-i[0]) ** 2 + (y2-i[1]) ** 2) < i[2]:
            x2_in_planet = 1
        result += x1_in_planet ^ x2_in_planet
    print(result)