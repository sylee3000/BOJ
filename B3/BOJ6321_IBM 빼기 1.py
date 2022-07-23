n = int(input())
for k in range(1, n + 1):
    name = input()
    replaced_name = []
    for i in name:
        if i == 'Z':
            replaced_name.append('A')
        else:
            replaced_name.append(chr(ord(i)+1))
    print(f'String #{k}')
    print(*replaced_name, sep='')
    print()