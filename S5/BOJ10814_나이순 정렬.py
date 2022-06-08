N = int(input())
member = []
for _ in range(N):
    age, name = input().split()
    member.append([int(age), name])
member = sorted(member, key=lambda k: k[0])
for i in member:
    print(i[0], i[1])