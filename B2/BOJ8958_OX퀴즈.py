test_case = int(input())
for i in range(test_case):
    result = [x for x in input()]
    total_score = 0
    correct_count = 0
    for x in result:
        if x == 'O':
            correct_count += 1
            total_score += correct_count
        else:
            correct_count = 0
    print(total_score)