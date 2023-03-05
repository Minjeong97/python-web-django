import sys
sys.stdin = open('input.txt')

T = int(input())

sticks_and_lasers = []

for tc in range(1, T+1):
    # 괄호들을 개별로 string으로 받기 위해 list 형태로 변환
    inputs = list(input())

    def dfs_inputs(inputs, '(', visited=[]):
        ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
        visited.append(start)

        for node in inputs[start]:
            if node not in visited:
                dfs_recursive(inputs, node, visited)
        return visited