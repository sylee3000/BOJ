K = int(input())

for j in range(1, K + 1):
    M, N = map(int, input().split())
    exam = {}
    for _ in range(M):
        course, day, time = input().split()
        time_left, time_right = time.split('-')
        start_time, start_minute = map(int, time_left.split(':'))
        end_time, end_minute = map(int, time_right.split(':'))
        start_time += round(start_minute / 60, 3)
        end_time += round(end_minute / 60, 3)
        exam[course] = (day, start_time, end_time)
    
    res = 0
    for _ in range(N):
        exam_list = list(input().split())
        p_exam = {}
        overlap = False
        for i in exam_list:
            d, s, e = exam[i]
            if d not in p_exam.keys():
                p_exam[d] = [(s, e)]
            else:
                for x in p_exam[d]:
                    if s < x[0] < e or e > x[1] > s or (s >= x[0] and e <= x[1]):
                        overlap = True
                        break
                if not overlap:
                    p_exam[d].append((s, e))
        if overlap:
            res += 1
    print(f"Data Set {j}:")
    print(res)