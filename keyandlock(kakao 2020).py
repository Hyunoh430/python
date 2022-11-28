def rotate(a):                          #90도 회전시키는 함수
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = result[i][j]
    return result


def check(newlock):                #열쇠가 맞는지 체크
    locklen = len(newlock) // 3
    for i in range(locklen, locklen * 2):
        for j in range(locklen, locklen * 2):
            if newlock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)
    newlock = [[0] * (n * 3) for _ in range(n * 3)]         #key를 여러방향으로 이동시키는걸 직접하지말고 lock을 확장시켜 대입 생각
    for i in range(n):
        for j in range(n):
            newlock[i + n][j + n] = lock[i][j]

    for rotation in range(4):                       #모든 방향 확인!
        key = rotate(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        newlock[x + i][y + j] += key[i][j]
                if check(newlock) == True:
                    return True                                     #열쇠가 맞는걸 확인했으니 종료!
                for i in range(m):
                    for j in range(m):
                        newlock[x + i][y + j] -= key[i][j]              #다시 원래 상태로 돌려놓기

    return answer