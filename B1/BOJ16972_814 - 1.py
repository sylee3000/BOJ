import random

for i in range(814):
    r = random.randrange(1, 5)
    if r == 1:
        print(random.random()*8140, random.random()*8140)
    elif r == 2:
        print(-random.random()*8140, random.random()*8140)
    elif r == 3:
        print(random.random()*8140, -random.random()*8140)
    else:
        print(-random.random()*8140, -random.random()*8140)