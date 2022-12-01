N = int(input())
array = list(map(int, input().split()))

def fixpoint(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1

    return None

result = fixpoint(array, 0, N - 1)
if result == None:
    print(-1)
else:
    print(result)
