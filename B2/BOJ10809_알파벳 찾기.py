alphabet_index = [-1] * 26
input_alphabet = input()
index = 0
for i in input_alphabet:
    if alphabet_index[ord(i) - ord('a')] < 0:
        alphabet_index[ord(i) - ord('a')] = index
    index += 1
    
result = [str(a) for a in alphabet_index]
print(" ".join(result))