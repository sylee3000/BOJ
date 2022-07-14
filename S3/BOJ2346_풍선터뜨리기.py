N = int(input())
paper_list = list(map(int, input().split(' ')))
pos = 0
index_list = [(i + 1) for i in range(N)]
print_list = []
while paper_list:
    next_index = paper_list[pos]
    print_list.append(index_list.pop(pos))
    paper_list.pop(pos)
    if paper_list:
        if next_index > 0:
            pos = (pos - 1 + next_index) % len(paper_list)
        else:
            pos = (pos + next_index) % len(paper_list)
print(*print_list)