vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    if word == 'end':
        break
    res = True
    vowel_in_word = False
    c, v = 0, 0
    last_word = ''
    for i in word:
        if i == last_word and i != 'e' and i != 'o':
            res = False
        else:
            if i in vowel:
                v += 1
                c = 0
                vowel_in_word = True
            else:
                v = 0
                c += 1
            if v >= 3 or c >= 3:
                res = False
        last_word = i
    if not vowel_in_word or not res:
        print(f'<{word}> is not acceptable.')
    else:
        print(f'<{word}> is acceptable.')