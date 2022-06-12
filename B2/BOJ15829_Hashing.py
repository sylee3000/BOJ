L = int(input())
string = input()
result = 0
index = 0
for i in string:
    result += ((ord(i)-ord('a')+1)*pow(31, index)) % 1234567891
    index += 1
print(result % 1234567891)