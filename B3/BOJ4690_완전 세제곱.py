import math

for a in range(2, 101):
    for b in range(2, 101):
        for c in range(b+1, 101):
            for d in range(c+1, 101):
                if math.pow(a, 3) == math.pow(b, 3) + math.pow(c, 3) + math.pow(d, 3):
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                if math.pow(a, 3) < math.pow(b, 3) + math.pow(c, 3) + math.pow(d, 3):
                    break