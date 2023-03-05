

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())  # 5, 2
    arr = [list(map(int, input().split())) for i in range(n)]  # [1, 3, 3, 6, 7]

    # n = 5, m = 2일 떄

    '''
    total += arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]
    total += arr[0][1] + arr[0][2] + arr[1][1] + arr[1][2]
    total += arr[0][2] + arr[0][3] + arr[1][2] + arr[1][3]
    total += arr[0][3] + arr[0][4] + arr[1][3] + arr[1][4]
                                ...
    total += arr[4][0] + arr[4][1] + arr[4][0] + arr[4][1]
    total += arr[4][1] + arr[4][2] + arr[4][1] + arr[4][2]
    '''
    max_sum = []  # 결과값 빈 리스트 생성

    for row in range(n - m + 1):  # 0 ~ 3
        for col in range(n - m + 1):  # 0 ~ 3
            sub_sum = 0
            for r in range(m):  # 0 ~ 1
                for c in range(m):  # 0 ~ 1
                    sub_sum += arr[row + r][col + c]
                    max_sum.append(sub_sum)

    print(max(max_sum))



