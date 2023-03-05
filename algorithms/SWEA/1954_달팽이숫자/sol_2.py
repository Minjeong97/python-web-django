import sys
sys.stdin = open('input.txt')

T = int(input())

# 방향 인덱스 설정 (우 > 하 > 좌 > 상)
row_direction = [0, 1, 0, -1]  # row
col_direction = [1, 0, -1, 0]  # col


for tc in range(1, T+1):
    # 주어진 n 값을 int 형태로 저장
    n = int(input())
    # 2차원 리스트 (n x n) 생성: 값은 0으로 채우기
    snail = [[0 for r in range(n)] for c in range(n)]

    # 처음 위치 설정
    r, c = (0, 0)  # 모든 TC에서 시작점은 (0, 0) 이다.

    # 초기 방향키 설정 (처음: '우')
    direction = 0  # (우: 0, 하: 1, 좌: 2, 상: 3)

    for n in range(1, n*n + 1):  # (N x N) 행렬 각 칸에 넣을 숫자 범위 (ex. 3x3 행렬은 1~9까지 들어감)
        snail[r][c] = n  # 처음 (0, 0) 칸에는 1이 들어감.

        r += row_direction[direction]  # 초기 행(row) 변동
        c += col_direction[direction]  # 초기 열(col) 변동  =>  결국, 첫 번째 행이 (1, 2, 3)으로 채워짐



        # 여기까지만 돌리면, index error가 난다. 그렇다면, 범위 오류를 없애고 방향을 바꿀 수 있는 작업이 필요함.
        # 따라서 n x n 행렬 범위 안에서, 초기값인 0이 아닌 다른 값이 이미 채워져 있다면 방향을 바꾸기 (일종의 벽을 만난다는 느낌.)
        if c < 0 or r < 0 or c >= n or r >= n or snail[r][c] != 0 or snail[r][c] < 0:
            # 벽을 만나면, 앞으로 가지 말고 뒤로 후진해라.
            if (r, c) == (0, n + 1):  # 만약 첫번째 행에서 마지막 열에 해당된다면 자리에서 멈추어라.

                r -= row_direction[direction]
                c -= col_direction[direction]

                # 방향을 틀어라
                direction += (direction + 1) % 4  # 초기값은 0, 그 다음은 1로 바뀌어야 함.

                # 튼 방향대로 다시 채우기
                r += row_direction[direction]
                c += col_direction[direction]

    print(f'#{tc} ')