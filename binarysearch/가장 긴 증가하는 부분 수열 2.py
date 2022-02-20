import sys
# 가장 긴 증가하는 부분 수열 2 : 12015번


def binary(target):
    start, end = 1, len(stack) - 1
    while start < end:
        mid = (start + end) // 2
        if stack[mid] < target:
            start = mid + 1
        elif stack[mid] > target:
            end = mid
        else:
            start = end = mid

    return end

start = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = [0]

for a in arr:
    if stack[-1] < a: # 스택의 끝 값보다 작으면
        stack.append(a) # 스택에 a값을 추가
    else:
        stack[binary(a)] = a


print(len(stack) - 1)