n = int(input())
k = int(input())    #사과 개수
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(k):  #사과 위치 기록
    x, y = map(int, input().split())
    graph[x][y] = 2     #사과는 2로 기록
l = int(input())    #방향 변환 횟수
data = []  #방향 정보
for i in range(l):
    a, b = map(str, input().split())
    data.append([int(a), b])   #a초후 b로 방향 전환

dx = [0, 1, 0, -1]  #우하좌상 (시작이 우이므로)
dy = [1, 0, -1, 0]

x, y = 1, 1
time = 0
direction = 0
length = 1
snake = [[1, 1]]
graph[x][y] = 1
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    time += 1
    for i in range(l):
        if data[i][0] == time:
            if data[i][1] == 'D':
                direction = (direction + 1) % 4
            elif data[i][1] == 'L':
                direction = (direction - 1) % 4


    #이제 이동한 뱀의 좌표로 조건들 따져보자!
    if nx < 1 or ny < 1 or nx > n or ny > n or graph[nx][ny] == 1:        #벽이나 몸에 박을 경우 종료
        print(time)
        break

    if graph[nx][ny] == 2:      #사과를 먹을 경우
        graph[nx][ny] = 1
        snake.append([nx, ny])


    elif graph[nx][ny] == 0:
        a, b = snake.pop(0)
        graph[a][b] = 0
        graph[nx][ny] = 1
        snake.append([nx, ny])
    x = nx
    y = ny


