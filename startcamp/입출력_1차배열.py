T = int(input())
for TestCase in range(1,T+1):

    data = list(map(int,input().split()))
    print(f"#{TestCase} {len(data)} {data[-1]}")
