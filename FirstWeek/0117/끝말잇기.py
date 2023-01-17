words = ["round" , "dream","magnet" ,"tweet","tweet", "trick", "kiwi"]
alreadySpoken = []
for i in range(len(words)) :
    if i == 0 :
        print(words[i])
        print(f"{i+1}번째 사람 성공!")
        alreadySpoken.append(words[i])
    elif i >0:
        print(words[i])
        if words[i-1][-1] == words[i][0] :
            if words[i] in alreadySpoken :
                print(f"{i+1}번째 사람 실패! 이미 했던 단어!")
                break
            else :
                print(f"{i+1}번째 사람 성공!")
                alreadySpoken.append(words[i])
        else :
            print(f"{i+1}번째 사람 실패! 말잇못!")
            break

# words 리스트에 임의의 단어를 추가해도 잘 작동한다.

        