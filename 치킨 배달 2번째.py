from itertools import combinations

n, m = map(int, input().split())
data = []
chicken = []
house = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 2:
            chicken.append([i, j])      #치킨집, 집 위치 입력받기
        elif data[i][j] == 1:
            house.append([i, j])

chicken_list = list(combinations(chicken, m))   #m개의 치킨 집 후보들
result = []
for i in range(len(chicken_list)):  #치킨집 후보들 하나씩 비교 해보자
    check = 0
    for j in range(len(house)):         #집에서 가장 가까운 치킨집 거리 구하기
        mini = 1e9
        for x, y in chicken_list[i]:    #치킨집 하나씩 비교
            distance = abs(x - house[j][0]) + abs(y - house[j][1])
            mini = min(mini, distance)  #가장 작은 거리를 구해 치킨거리 구하기
        check += mini
    result.append(check)         #도시의 치킨거리

print(min(result))      #모든 도시의 치킨거리 중 제일 작은 값 출력


