T = int(input())
for TestCase in range(1,T+1):
    star = '*'
    blank = ' '
    star_num = int(input())
    blank_num = star_num - 1
    print(f"#{TestCase}")
    for i in range(1,star_num + 1) :
        print((blank_num * blank) + (star * i))
        blank_num -=1
