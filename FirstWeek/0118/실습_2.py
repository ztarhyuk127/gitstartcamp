s = input()

if len(s) % 2 == 0 : # len(s) = 26이면 0~25의 길이를 갖는다. 12,13 출력해야함.
    print(s[int(len(s)/2)-1 : int(len(s)/2)+1])
else :
    print(s[int(len(s)//2)])