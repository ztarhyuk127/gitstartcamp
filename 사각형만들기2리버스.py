T = int(input())
for TestCase in range(1,T+1) :
    print(f"#{TestCase}")

    h,w = map(int,input().split())
    num = 1
    for i in range(0,h) :
        for j in range(0,w):
            print(num + (j * h), end = " ")
        num +=1
        print()


