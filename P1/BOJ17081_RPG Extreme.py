N, M = map(int, input().split())
grid = []
start = None # 시작 위치
monster_count = 0 # 몬스터 개체 수
box_count = 0 # 아이템 상자 개수
move = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
move_count = 0

for i in range(N):
    line = list(input())
    for k in line:
        if k == '@': # 시작 위치가 있을 때
            j = line.index('@') # 위치를 찾고
            start = [i, j]# start에 저장
        if k == '&' or k == 'M':
            monster_count += 1
        if k == 'B':
            box_count += 1
    grid.append(line)
    
S = input() # 이동 방법

monster = {}
for _ in range(monster_count): # 몬스터 정보 저장
    monster_info = input().split()
    monster[(int(monster_info[0]) - 1, int(monster_info[1]) - 1)] = {
        'name' : monster_info[2],
        'ATT' : int(monster_info[3]),
        'DEF' : int(monster_info[4]),
        'HP' : int(monster_info[5]),
        'EXP' : int(monster_info[6])
    }

item_box = {}
for _ in range(box_count): # 아이템 상자 저장
    box_info = input().split()
    item_box[(int(box_info[0]) - 1, int(box_info[1]) - 1)] = {
        'TYPE' : box_info[2],
        'S' : box_info[3]
    }
    
index = start
last_step = '.'
user = {
    'LV' : 1,
    'HP' : 20,
    'MAX_HP' : 20,
    'ATT' : 2,
    'EQUIPPED_ATT' : 0,
    'DEF' : 2,
    'EQUIPPED_DEF' : 0,
    'EXP' : 0,
    'REQUIRED_EXP' : 5,
    'ACC' : []
}
death_by = ''
spike_damage = 5
for i in S: # 순서대로 수행
    move_count += 1
    next_x = index[0] + move[i][0] # 다음 단계의 x 위치
    next_y = index[1] + move[i][1] # 다음 단계의 y 위치
    next_index = [next_x, next_y]
    grid[index[0]][index[1]] = '.'
    # 다음 단계의 위치가 grid 안이거나 다음 단계가 벽이 아닐 때
    if 0 <= next_x < N and 0 <= next_y < M and grid[next_x][next_y] != '#':
        if last_step == '^':
            grid[index[0]][index[1]] = '^'
        index = next_index
    else: # 이전 단계를 한번 더 수행
        grid[index[0]][index[1]] = last_step
    
    if grid[index[0]][index[1]] == '.': # 빈 칸
        last_step = grid[index[0]][index[1]]
        grid[index[0]][index[1]] = '@'
        continue
    elif grid[index[0]][index[1]] == 'B': # 상자 칸
        if item_box[(index[0], index[1])]['TYPE'] == 'O': # 장신구 상자
            if item_box[(index[0], index[1])]['S'] in user['ACC']: # 이미 존재하는 장신구일 때
                continue
            user['ACC'].append(item_box[(index[0], index[1])]['S'])
            if item_box[(index[0], index[1])]['S'] == 'HR':
                pass
            elif item_box[(index[0], index[1])]['S'] == 'RE':
                pass
            elif item_box[(index[0], index[1])]['S'] == 'CO':
                pass
            elif item_box[(index[0], index[1])]['S'] == 'EX':
                pass
            elif item_box[(index[0], index[1])]['S'] == 'DX': # DX : 가시 데미지 1로 고정
                spike_damage = 1
            elif item_box[(index[0], index[1])]['S'] == 'HU':
                pass
            elif item_box[(index[0], index[1])]['S'] == 'CU':
                pass
        else:
            if item_box[(index[0], index[1])]['TYPE'] == 'W':
                user['EQUIPPED_ATT'] = int(item_box[(index[0], index[1])]['S'])
            else:
                user['EQUIPPED_DEF'] = int(item_box[(index[0], index[1])]['S'])
        last_step = '.'
        grid[index[0]][index[1]] = '@'
        continue
    elif grid[index[0]][index[1]] == '^':
        last_step = grid[index[0]][index[1]]
        user['HP'] -= spike_damage 
        if user['HP'] <= 0:
            user['HP'] = 0
            death_by = '^'
            break
        grid[index[0]][index[1]] = '@'
    elif grid[index[0]][index[1]] == '&':
        last_step = '.'
        p_mon = monster[(index[0], index[1])]
        turn = 1
        while user['HP'] > 0 and p_mon['HP'] > 0:
            if turn % 2 == 1:
                p_mon['HP'] -= max(1, (user['ATT'] + user['EQUIPPED_ATT']) - p_mon['DEF'])
            else:
                user['HP'] -= max(1, p_mon['ATT'] - (user['DEF'] + user['EQUIPPED_DEF']))
            turn += 1
        if user['HP'] <= 0:
            user['HP'] = 0
            death_by = p_mon['name']
            break
        else:
            user['EXP'] += p_mon['EXP']
            if user['EXP'] >= user['REQUIRED_EXP']:
                user['LV'] += 1
                user['EXP'] = 0
                user['REQUIRED_EXP'] += 5
                user['MAX_HP'] += 5
                user['HP'] = user['MAX_HP']
                user['ATT'] += 2
                user['DEF'] += 2
            grid[index[0]][index[1]] = '@'
for i in range(N):
    for j in range(M):
        print(grid[i][j], end='')
    print()
print(f'Passed Turns : {move_count}')
print(f'LV : {user["LV"]}')
print(f'HP : {user["HP"]}/{user["MAX_HP"]}')
print(f'ATT : {user["ATT"]}+{user["EQUIPPED_ATT"]}')
print(f'DEF : {user["DEF"]}+{user["EQUIPPED_DEF"]}')
print(f'EXP : {user["EXP"]}/{user["REQUIRED_EXP"]}')
if death_by == '^':
    print('YOU HAVE BEEN KILLED BY SPIKE TRAP..')
elif death_by != '':
    print(f'YOU HAVE BEEN KILLED BY {death_by}..')