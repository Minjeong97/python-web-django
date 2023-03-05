import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 주어진 n 값을 int 형태로 저장
    n = int(input())

    # 2차원 리스트 (n x n) 생성 (단, 1로 모두 채우고 나서 1씩 더하는 형식)
    snail = [[0 for r in range(n)] for c in range(n)]
    # print(snail)

    for r in range(n):  # 0행 반복문: if n=3, 0~2
        for c in range(n):
            if r == 0:
                snail[r][c] = c+1
    # print(snail)






    print(f'#{tc} ')

'''
snail[0][0] = 1
snail[0][1] = 2
snail[0][2] = 3
----> 여기까지는 고정
snail[1][2] = 4
snail[2][2] = 5

snail[2][1] = 6
snail[2][0] = 7

snail[1][0] = 8
snail[1][1] = 9
'''