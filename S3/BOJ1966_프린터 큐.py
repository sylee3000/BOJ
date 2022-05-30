from collections import deque

TestCase = int(input())
count = 1

for i in range(TestCase):
    N, target = map(int, input().split())
    print_list = deque([0 for _ in range(N)])
    print_list[target] = 1
    priority = deque([x for x in map(int, input().split())])
    while print_list:
        max_p = max(priority)
        p = priority.popleft()
        t = print_list.popleft()
        print(max_p, p, t, count)
        if max_p == p:
            if t == 1:
                print(count)
                count = 1
                break
            else:
                count += 1
        else:
            print_list.append(t)
            priority.append(p)