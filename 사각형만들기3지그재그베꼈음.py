T = int(input())
for TestCase in range(1,T+1):

    n , m = map(int,input().split())

    arr_2d = [
        [0 for _ in range(m)]  # N은 행, M은 열
        for _ in range(n)
    ]
    count = 1
    print(f"#{TestCase}")
    for row in range(n):
        if row % 2 == 0 : # 행이 홀수냐??
            for col in range(m): # 0 1 2 3 4
                arr_2d[row][col] = count #arr_2d[0][0~4]
                count += 1
        elif row % 2 != 0 : # 행이 짝수냐??
            for col in range(m-1,-1,-1): # 4 3 2 1 0
                arr_2d[row][col] = count # arr_2d[1][4~0]
                count += 1


    for row in range(n):
        for col in range(m):
            print(arr_2d[row][col], end =" ")
        print()
