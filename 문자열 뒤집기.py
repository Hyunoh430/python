data = input()
check0 = 0
check1 = 0

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':      #0에서 1로 몇번 바뀌나
            check1 += 1
        if data[i + 1] == '0':      #1에서 0으로 몇번 바뀌나
            check0 += 1

if data[0] == '0':
    check0 += 1
else:
    check1 += 1
print(min(check0, check1))



