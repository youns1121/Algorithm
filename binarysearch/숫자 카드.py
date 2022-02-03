from sys import stdin

N = int(stdin.readline())
N_card = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
M_card = list(map(int, stdin.readline().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(M):
    if binary_search(N_card, M_card[i], 0, N - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')