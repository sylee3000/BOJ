M = int(input())
number_of_digits = 1
odd_number = 0
even_number = 0
while True:
    if M > 2 ** ((number_of_digits - 1) // 2):
        M -= 2 ** ((number_of_digits - 1) // 2)
        if number_of_digits % 2 == 1:
            odd_number += 2 ** ((number_of_digits - 1) // 2)
        else:
            even_number += 2 ** ((number_of_digits - 1) // 2)
        number_of_digits += 1
    else:
        if number_of_digits % 2 == 1:
            odd_number += M
        else:
            even_number += M
        break
if number_of_digits % 2 == 1:
    part_n = bin(odd_number)[2:]
    all_n = '0b' + part_n + part_n[-2::-1]
else:
    part_n = bin(even_number)[2:]
    all_n = '0b' + part_n + part_n[::-1]
print(int(all_n, 2))