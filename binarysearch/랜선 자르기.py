from sys import stdin

K, N = map(int, stdin.readline().split())
lan=[]


for i in range(K): # 가지고 있는 랜선의 수 만큼 랜선 길이 입력받기
 lan.append(int(stdin.readline()))

start, end = 1, max(lan) # 시작값, 끝값

while start <= end:
    lines = 0 # 랜선 수

    mid = (start + end) // 2

    for i in lan: # 랜선길이 별로 mid 값으로 나눠서 랜선 수 구하기
        lines += i // mid

    if(lines >= N): #필요 갯수보다 랜선수가 같거나 클 때
        start = mid+1
    else:
        end = mid -1

print(end)



