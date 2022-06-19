V = int(input())
vote = input()
A_vote = 0
B_vote = 0
for i in vote:
    if i == 'A':
        A_vote += 1
    else:
        B_vote += 1
if A_vote > B_vote:
    print('A')
elif A_vote < B_vote:
    print('B')
else:
    print('Tie')