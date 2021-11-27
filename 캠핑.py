cnt = 0 # 카운트

while True:

    # 총 V일간의 휴가기간동안 캠핑장을 연속하는 P일 중, L일동안 이용가능
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    C = (V // P) * L # (휴가기간중 캠핑장을 P일을 이용할 수 있는 횟수) * 캠핑장 이용 가능한 일 수
    N = min((V % P), L) # 최소(휴가기간중 캠핑장을 P일을 전부 이용하고 남는 휴일, 캠핑장 이용 가능한 일 수)
    day = C + N
    cnt += 1
    print("Case %d: %d" % (cnt, day))










