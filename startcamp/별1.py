T = int(input())
for TestCase in range(1,T+1) :
    star_num = int(input())
    star_lim = 1
    print(f"#{TestCase}")
    while star_lim <= star_num :
        print('*' * star_lim)
        star_lim +=  1