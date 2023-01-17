from copy import deepcopy
#상하좌우 이동했을때의 함수를 구현
def move_left(data):
    for i in range(n):
        num = 0
        for j in range(n):
            if data[i][j] != 0:
                check = data[i][j]
                data[i][j] = 0
                data[i][num] = check
                for k in range(j + 1, n):
                    if data[i][k] != 0 and data[i][k] != check:
                        break
                    if check == data[i][k]:
                        data[i][k] = 0
                        data[i][num] *= 2
                        break
                num += 1
    return data
def move_right(data):
    for i in range(n):
        num = n - 1
        for j in range(n - 1, -1, -1):
            if data[i][j] != 0:
                check = data[i][j]
                data[i][j] = 0
                data[i][num] = check
                for k in range(j - 1, -1, -1):
                    if data[i][k] != 0 and data[i][k] != check:
                        break
                    if check == data[i][k]:
                        data[i][k] = 0
                        data[i][num] *= 2
                        break
                num -= 1
    return data
def move_down(data):
    for i in range(n):
        num = n - 1
        for j in range(n - 1, -1, -1):
            if data[j][i] != 0:
                check = data[j][i]
                data[j][i] = 0
                data[num][i] = check
                for k in range(j - 1, -1, -1):
                    if data[k][i] != 0 and data[k][i] != check:
                        break
                    if check == data[k][i]:
                        data[k][i] = 0
                        data[num][i] *= 2
                        break
                num -= 1
    return data
def move_up(data):
    for i in range(n):
        num = 0
        for j in range(n):
            if data[j][i] != 0:
                check = data[j][i]
                data[j][i] = 0
                data[num][i] = check
                for k in range(j + 1, n):
                    if data[k][i] != 0 and data[k][i] != check:
                        break
                    if check == data[k][i]:
                        data[k][i] = 0
                        data[num][i] *= 2
                        break
                num += 1
    return data
#이제 최대 5번 이동시켜 최댓값 구해보자
n = int(input())
data1 = []
for i in range(n):
    data1.append(list(map(int, input().split())))




def dfs(data, check):
    global maxnum
    if check == 5:      #원래 상태로 어떻게 돌리지???
        for i in range(n):
            for j in range(n):
                maxnum = max(maxnum, data[i][j])
        return
    #print(move_right(deepcopy(data)))
    dfs(move_right(deepcopy(data)), check + 1)
    dfs(move_left(deepcopy(data)), check + 1)
    dfs(move_down(deepcopy(data)), check + 1)
    dfs(move_up(deepcopy(data)), check + 1)


maxnum = -1e9
dfs(data1, 0)
print(maxnum)

