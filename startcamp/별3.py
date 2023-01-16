T = int(input())
for TestCase in range(1,T+1):
    print(f"#{TestCase}")
    star_num, star_shape = map(int,input().spllit())
    star = '*'
    blank * ' '

    if star_shape == 1:
        star_lim = 1
        print(f"#{TestCase}")
        while star_lim <= star_num :
            print('*' * star_lim)
            star_lim +=  1


    elif star_shape ==2:


    elif star_shape ==3:





