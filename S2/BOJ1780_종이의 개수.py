import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0, 0] # -1, 0, 1 개수
def paper_divide(x, y, K):
    number_list = paper[x][y]
    paper_count[number_list + 1] += 1
    for i in range(x, x + K):
        for j in range(y, y + K):
            if paper[i][j] != number_list:
                paper_count[number_list + 1] -= 1
                for i in range(x, x + K, K // 3):
                    for j in range(y, y + K, K // 3):
                        paper_divide(i, j, K // 3)
                return
paper_divide(0, 0, N)
for i in range(3):
    print(paper_count[i])