T = int(input())
for TestCase in range(1,1+T):
    N , M = map(int,input().split)
    multi = 1
    while N * multi < M :
        print({N * multi})
        multi += 1

