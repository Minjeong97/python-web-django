import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 5, 2
    arr = [list(map(int, input().split())) for i in range(N)]

"""
    m[0][0]+m[0][1]+m[0][2], m[0][1]+m[0][2]+m[0][3], m[0][2]+m[0][3]+m[0][4], m[0][3]+m[0][4]+m[0][5]
    m[1][0]+m[1][1]+m[1][2], m[1][1]+m[1][2]+m[1][3], m[1][2]+m[1][3]+m[1][4], m[1][3]+m[1][4]+m[1][5]
    m[2][0]+m[2][1]+m[2][2], m[2][1]+m[2][2]+m[2][3], m[2][2]+m[2][3]+m[2][4], m[2][3]+m[2][4]+m[2][5]

    m[3][0]+m[3][1]+m[3][2], m[3][1]+m[3][2]+m[3][3], m[3][2]+m[3][3]+m[0][4], m[3][3]+m[3][4]+m[3][5]
    m[4][0]+m[4][1]+m[4][2], m[4][1]+m[4][2]+m[4][3], m[4][2]+m[4][3]+m[1][4], m[4][3]+m[4][4]+m[4][5]
    m[5][0]+m[5][1]+m[5][2], m[5][1]+m[5][2]+m[5][3], m[5][2]+m[5][3]+m[2][4], m[5][3]+m[5][4]+m[5][5]
"""
for row in range(N):  # N = 9, 0 ~ 8
    for col in range(0, row + M):  # 1, 4
        data += matrix[col][row]  # [0][]
    result.append(data)




'''
def hit(row, col):
    
    
    return  # 파리수
    
    
'''