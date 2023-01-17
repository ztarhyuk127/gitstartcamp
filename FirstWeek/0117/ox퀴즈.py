T = int(input())
for TestCase in range(1,T+1):
    oxmark= input() # OX로 된 문자열
    totalScore = 0  # 총점
    score = 0       # 현재점수
    if oxmark[0] == 'O' : #첫문자 O일 때
        score += 1
        totalScore += 1        
    for i in range(1,len(oxmark)) :
        if oxmark[i] == 'O' :  #2문자 O일때
            if oxmark[i] == oxmark[i-1] : # oo
                score += 1 #현재점수 +1
                totalScore += score #총점 + 현점
            elif oxmark[i] != oxmark[i-1] :# xo
                score += 1
                totalScore += 1
        elif oxmark[i] =='X':
            score = 0
    print(totalScore)



'''
000
123 6

00x
120 3

0x0 
101 2

x00
012 3

0xx
'''