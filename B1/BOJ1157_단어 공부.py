word = input().upper()
word_dict = {}
for i in word:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] += 1
max_count = 0
max_key = ''
for key, value in word_dict.items():
    if value > max_count:
        max_key = key
        max_count = value
    elif value == max_count:
        max_key = "?"
print(max_key) 
