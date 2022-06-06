N = int(input())
count = 0
for _ in range(N):
    word = input()
    alphabet_list = []
    is_group_word = 1
    last_alphabet = ''
    for i in word:
        if i in alphabet_list and i != last_alphabet:
            is_group_word = 0
            break
        else:
            last_alphabet = i
            if i not in alphabet_list:
                alphabet_list.append(i)
    count += is_group_word
    
print(count)
            