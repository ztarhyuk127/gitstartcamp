def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    # problem01 최고점을 반환하는 함수
    maxone = 0
    for i in range(len(scores)) :
        for j in range(len(scores)):
            if scores[i] < scores[j]:
                maxone = scores[j]
        else :
            continue
    return maxone


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60 , 90, 70]
    print(max_score(scores)) # 90
