import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = input()

    # Step 1. stick braket과 laser가 구분된 리스트 만들기
    bars = []  # ['laser', '(', '(', '(', 'laser', 'laser', ')', '(', 'laser', ')', 'laser', ')', ')', '(', 'laser', ')']
    for i in range(len(N)):
        if (N[i] == '(') and (N[i+1] == ')'):
            bars.append('laser')
        elif (N[i] == ')') and (N[i-1] == '('):
            continue

        else:
            bars.append(N[i])
    # print(f'{tc} {bars}')

    # Step 2. 왼쪽부터 차례대로 '('와 ')'의 index 값을 넣은 list를 만들기

    idxes = []
    for idx in range(len(bars)):
        idxes.append((bars[idx], idx))
    # print(idxes)

    # laser, bra, ket 에 대한 index 딕셔너리 만들기
    '''
    {
    '(': [0, 1, 2, 4, 9, 15], 
    'laser': [3, 5, 6, 10, 12, 16, 17], 
    ')': [7, 8, 11, 13, 14, 18]
    }
    '''
    from collections import defaultdict
    dict_lists = defaultdict(list)

    for k, v in idxes:
        dict_lists[k].append(v)

    print(dict_lists)

    laser_lists = dict_lists['laser']
    bra_lists = dict_lists['(']  # [0, 1, 2, 4, 9, 15]
    ket_lists = dict_lists[')']  # [7, 8, 11, 13, 14, 18]

    print(bra_lists, ket_lists)

    # Step 3. '('에 해당되는 index를 기준으로, '('의 index와의 뺄셈 경우의 수를 계산 => 그 차이가 가장 최소화되는 braket index 찾기
    total_diff = []
    for k in range(len(ket_lists)):
        diff = []
        for b in range(len(bra_lists)):
            if bra_lists[b] < ket_lists[k]:  # ')' 위치 인덱스보다 '('가 앞에 위치해 있을 때만 계산해야 함.
                diff.append(abs(bra_lists[b] - ket_lists[k]))  # 절대값
            else:
                diff.append(len(bars))  # 16, 19  ==> 언제나 len(bar) 보다 숫자가 크지 않으니까.
        total_diff.append(diff)  # ket_lists 안의 요소들 개수 만큼, 뺄셈 경우의 수 결과에 대한 2차원 리스트가 형성됨.
    print(total_diff)
    # 즉, ')'에 대해 순차적으로 '(' 위치를 뺀 값의 리스트에서 최소값을 찾으면, 각 ')'에 대한 최소값을 찾을 수 있음.  (또한, 리스트 안의 리스트 개수는 막대기 개수와 같음.)
    # 그렇다면, 이제 각 ket_lists의 최솟값만 뽑아내보자.
    min_idx = []
    for tdi in range(len(total_diff)):
        num = total_diff[tdi]
        min_idx.append(num.index(min(num)))  # 최솟값에 해당되는 index 추출
    print(min_idx)  # '('에 해당되는 딕셔너리 리스트 value 값의 인덱스
    # 결국, min_idx의 각 요소값 (min value를 가진 total_diff 각 리스트 안의 index) = 각 ')'의 가장 가까운 '(' index 값 => '(' lists & ')' lists 에서.

    # Step 4. 막대기 매칭
    # bra 위치(min_idx의 value)와 ket 위치(min_idx의 index)에 접근해서 string_n 로 바꾸기 (n = 막대기 개수)
    stick_and_laser = bars
    for mi in range(len(min_idx)):  # [2, 3, 3, 3, 4]: 0 ~ 4
        k, v = mi, min_idx[mi]  # index, value
        # total_

        if ket_lists.index(ket_lists[k]) == min_idx.index(v):
            stick_and_laser[total_diff[mi][v]] = stick_and_laser[ket_lists[k]] = mi
        #[mi if x==stick_and_laser[bra_lists[k]] else x for x in stick_and_laser]
        #stick_and_laser[bra_lists[k]] = mi
        #[mi if x==stick_and_laser[bra_lists[v]] else x for x in stick_and_laser]
        #stick_and_laser[ket_lists[mi]] = mi

        # stick_and_laser.append(bra_lists[min_idx[mi]])  # ex. min_idx[0]: 2 => bra_lists[2]: 3
        # stick_and_laser.append(ket_lists[mi])  # ket_lists[0]: 6

    print(stick_and_laser)












'''    for idx in range(len(bars)):
        if bars[idx] != 'laser':
            idxes.append([idx, bars[idx]])
    print(idxes)
'''
'''
    # enumerate 함수 사용해도 괜찮음.
    for idx, value in enumerate(bars):
        idxes = idx, value
'''


'''
    bra_list = [b[0] for b in idxes if idxes[b][1][:] == '(']
    print(bra_list)
    ket_list = [k[0] for k in idxes if idxes[k][1][:] == ')']
    print(ket_list)
    '''

'''
    bra_list = [b for b in range(len(idxes)) if '(' in idxes[b][1]]
    print(bra_list)
    ket_list = [k for k in range(len(idxes)) if ')' in idxes[k][1]]
    print(ket_list)
'''

'''    bra_list = []
    ket_list = []
    for i in range(len(idxes)):  # range: (0 ~ 9), (0 ~ 11)
        if idxes[i][1] == '(':  # '(' 기준으로 계산할 것.
            if idxes.find(')'):
                diff.append(idxes[fi][0] - )'''


