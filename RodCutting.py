#나무 자르기
def solution(a, n):
    answer1 = [0]
    answer2 = 0


    for j in range(1, n + 1):
        for i in range(j):
            answer2 = max(answer2, a[j - i] + answer1[i])
        answer1.append(answer2)
    return answer1[n]


print(solution([0,1,5,8,9,10,17,18,20,24,30], 9))
