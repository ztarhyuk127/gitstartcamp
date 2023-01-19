# chr() : 숫자 -> 코드
# ord() : 코드 -> 숫자

def get_secret_word(a) :
    for i in a :
        print(chr(i),end='')

get_secret_word([83,115,65,102,89])