import sys
sys.stdin = open('input.txt')

T = int(input())

sticks_and_lasers = []

for tc in range(1, T+1):
    # 괄호들을 개별로 string으로 받기 위해 list 형태로 변환
    inputs = list(input())
    # print(inputs)
    print(len(inputs))  # 22, 26
    '''
    ['(', ')', '(', '(', '(', '(', ')', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')', ')', '(', '(', ')', ')']
    [1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1]
    [0, 0, 1, 1, 1, 0, 0, 0, 0, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 0, 0, -1]
    '''


    # 바로 앞뒤로 '(' + ')' 가 있으면 하나로 묶기.
    for idx in range(len(inputs)):  # 문제에서 주어진 전체 괄호 리스트 길이 만큼의 idx 반복문 => 문자열 하나씩 앞뒤 탐색
        if inputs[idx] == '(':  # 만약 각 index 기준으로, '(' 로 시작할 때,
            if inputs[idx+1] == ')':  # 바로 뒤에 ')'가 있으면 => * 왼쪽부터 차례대로 들어가니까 기준이 되는 것은 '('이다.
                sticks_and_lasers.append(inputs[idx] + inputs[idx+1])  # '()' 형태로 합쳐서 저장
            else:
                sticks_and_lasers.append(inputs[idx])
        # elif inputs[idx] == ')':
            sticks_and_lasers.append(inputs[idx])
        # elif inputs[idx] != '(' or inputs[idx] == ')':  # 만약 '('가 아니거나, ')'로 시작한다면 그냥 append
        #     sticks_and_lasers.append(inputs[idx])

print(sticks_and_lasers)






    #print(f'#{tc} ')
