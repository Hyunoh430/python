from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))       #미로 입력받기
#최단거리 구하기 => bfs
dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]      #상하좌우 방향 설정

def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:            #큐가 비어있을때 까지 실행
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:     #이걸 안하면 list index out of range랑 graph[-1][-1] 이런게 인식 가능해서 무조건 해줘야함
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                q.append([nx, ny])

bfs(0,0)

# for i in range(n):
#     for j in range(m):
#         print(graph[i][j], end = '.')
#     print()

print(graph[n -1][m - 1])
