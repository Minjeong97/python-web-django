import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    matrix = [[0 for _ in range(10)] for _ in range(10)]  # 10*10 행렬
    
    # 색칠 시작
    for _ in range(N):
        a = list(map(int, input().split()))  # [2, 2, 4, 4, 1] = [시작r, 시작c, 끝r, 끝c, 색깔]
        print(a)


    print(f'#{tc} ')