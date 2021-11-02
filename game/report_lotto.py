import random

def lotto(count):

        for i in range(count): # 0부터 count 까지 반복
            lotto_num = [] # 로또 번호가 담길 리스트형 변수

            for j in range(6): # 6번 반복

                rand_num = random.randint(1, 45) # 1~45 난수생성
                while rand_num in lotto_num: #중복될 경우
                    rand_num = random.randint(1, 45)  #다시 난수생성
                lotto_num.append(rand_num) # 난수를 변수에 담음, 중복되지 않은경우

            lotto_num.sort() # 오름차순 정렬
            print("{}. 로또번호: {}".format(i+1, lotto_num))

lotto(5) # 로또 생성 갯수




