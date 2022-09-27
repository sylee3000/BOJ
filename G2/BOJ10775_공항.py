import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

gate = {}
for i in range(G + 1):
    gate[i] = i
    
res = 0
docking = True
    
for i in range(P):
    g_i = int(input())
    while g_i > gate[g_i] and g_i > 0 and docking:
        temp = gate[g_i]
        if temp > 0:
            gate[g_i] = gate[g_i] - 1
            g_i = temp
        else:
            docking = False
    if g_i > 0 and docking:
        if gate[g_i] == g_i:
            gate[g_i] -= 1
            res += 1
print(res)