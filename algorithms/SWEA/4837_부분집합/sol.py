import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

        map(int, input().split())  # [1, 1, 3, 3, 1] = [시작r, 시작c, 끝r, 끝c, 색깔]

    print(f'#{tc} ')