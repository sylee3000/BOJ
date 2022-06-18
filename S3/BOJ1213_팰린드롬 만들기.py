english_name = input()
word_dict = {}
for i in english_name:
    if i not in word_dict.keys():
        word_dict[i] = 1
    else:
        word_dict[i] += 1
word_dict = dict(sorted(word_dict.items()))
mid = 0
mid_word = ''
pal = ''
for key, value in word_dict.items():
    if value % 2 == 1:
        if value > 2:
            for _ in range(value // 2):
                pal = pal + key
        mid += 1
        mid_word = key
    else:
        for _ in range(value // 2):
            pal = pal + key
if mid > 1:
    print("I'm Sorry Hansoo")
elif mid == 1:
    print(pal + mid_word + pal[::-1])
else:
    print(pal + pal[::-1])