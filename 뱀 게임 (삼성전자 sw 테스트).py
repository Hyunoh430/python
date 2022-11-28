N = int(input())        #보드의 크기
K = int(input())        #사과의 개수
board = [[0] * N for _ in range(N)]  # N * N 보드판 만들기
#사과의 위치를 1로 입력하자
for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1             #1행1열이 [0,0]
L = int(input())        #뱀의 방향 변환 횟수
data = []             # (X, C 입력) X초 끝난 뒤 C(L왼쪽, D오른쪽) 방향으로 회전
for i in range(L):
    data.append(list(input().split()))
    data[i][0] = int(data[i][0])

dx = [0, 1, 0, -1]  #동,남,서,북 (처음 동쪽 보고 있음)
dy = [1, 0, -1, 0]
def rotate(direction, C):
    if C == 'L':
        direction = ((direction) - 1) % 4       #방향전환 해주기
    elif C == 'D':
        direction = ((direction) + 1) % 4
    return direction

x, y = 0, 0     #snake location 머리 위치
board[x][y] = 2 #snake위치는 2로 저장
direction = 0  # 초기 방향 동쪽 보니 0으로
time = 0
snake = [(x, y)] #snake 몸통

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    time += 1           #일단 실행 됐으니 1초 증가
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:      #벽에 박거나 자기 몸이랑 만날 경우 종료
        print(time)
        break
    for i in range(L):
        if (time == data[i][0]):        #뱡향 전환 정보 체크
            direction = rotate(direction, data[i][1])
    if board[nx][ny] == 1:                    #뱀의 머리가 사과 만날경우
        board[nx][ny] = 2               #뱀 위치 기록
        snake.append((nx, ny))          #뱀 몸통 기록(기존 몸 제거 할 필요 없음)
    elif board[nx][ny] == 0:
        a, b = snake.pop(0)             #기존 몸 제거
        board[a][b] = 0
        board[nx][ny] = 2           #뱀 위치 기록
        snake.append((nx, ny))
    x = nx                          #모든 상황 종료 후 x, y 값 새로 받깆
    y = ny








