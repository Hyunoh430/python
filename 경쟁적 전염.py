from collections import deque

n, k = map(int, input().split())
array = []
data = []   #바이러스의 위치정보
for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(n):
        if array[i][j] != 0:
            data.append([array[i][j], 0, i, j])      #바이러스의 종류, 시간, 좌표 입력
s, x, y = map(int, input().split())
data.sort()     #data 정렬하기
dx = [-1, 1, 0, 0]      #상하좌우 방향 설정
dy = [0, 0, -1, 1]

q = deque(data)
while q:            #큐가 빌때까지 실행
    virus, time, fx, fy = q.popleft()
    if time == s:       #만약 이제 실행할라는 것이 목표시간이라면???
        break
    for i in range(4):      #상하좌우로 바이러스 퍼트리기 시작
        nx = fx + dx[i]
        ny = fy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:      #벽을 넘어서면 취소
            continue
        if array[nx][ny] == 0:          #비어있는 곳이라면 바이러스 넣기
            array[nx][ny] = virus
            q.append([virus, time + 1, nx, ny]) #큐에 추가

print(array[x - 1][y - 1])
