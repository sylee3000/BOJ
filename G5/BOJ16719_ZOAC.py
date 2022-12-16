alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string = input()
res = [string]

while string:
    s_len = len(string)
    point = s_len - 1
    if s_len == 1:
        break
    for i in range(s_len - 1):
        if alphabet.index(string[i]) > alphabet.index(string[i + 1]):
            point = i
            break
    string = string[:point] + string[point+1:]
    res.append(string)
while res:
    print(res.pop())