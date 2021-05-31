# n, m, k 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))


data.sort(reverse=True)

first = data[0]
second = data[1]

result = 0

while m != 0 :
    for i in range(k): # 큰수 k번 반복
        result += first
        m -= 1
    result += second
    m -= 1


print(result)

