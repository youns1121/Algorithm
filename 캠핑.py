from sys import stdin

cnt = 0

while True:
    L, P, V = map(int, stdin.readline().split()) # 5 8 20
    #이는 총 V일간의 휴가기간동안 캠핑장을 연속하는 P일 중, L일동안 이용가능
    cnt += 1
    if L == 0 and P == 0 and V == 0:
        break

    a = V // P # 휴가기간중에 캠핑장을 P일을 전부 이용할 수 있는 횟수 // 2번
    b = V % P # 휴가기간(20일)중에 캠핌장을 P일을 전부 이용하고 남는 휴일  4일

    if L < b: # 캠핑장 사용가능한일 수가 휴가중에 캠핑장을 이용하고 남는 휴일보다 작을때
        a = L

    print("Case %d: %d" %(cnt, (a * L) + b)) # 캠핑장 P일 전부 이용가능한 횟수 * 캠핑장 이용가능일 + 남는 휴일


