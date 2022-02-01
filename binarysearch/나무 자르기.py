from sys import stdin


N, M = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))

start, end = 1, max(tree) #시작점, 끝점

while start <= end:

    namu = 0  # 벌목된 나무 초기화
    mid = (start + end) // 2
    for i in tree:
        if i > mid: # 인덱스의 값이 절단기 높이 보다 큰 경우
            namu += i - mid # 인덱스 값에 절단기 값으로 뺀다

    if namu >= M:
        start = mid + 1 # 필요한 벌목 나무 길이보다 더 많이 잘렸으면
    else:
        end = mid - 1 # 필요한 벌목 나무 길이보다 덜 잘렸으면

print(end)






