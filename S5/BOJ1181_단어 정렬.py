import sys
input = sys.stdin.readline

N = int(input())
word_list = []
max_len = 0
for _ in range(N):
    word = input()
    if word not in word_list:
        word_list.append(word)
    max_len = max(max_len, len(word))
for i in range(1, max_len + 1):
    word_l = []
    for j in word_list:
        if len(j) == i:
            word_l.append(j)
    word_l = sorted(word_l)
    for j in word_l:
        print(j, end='')
