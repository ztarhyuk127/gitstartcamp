T = int(input())
for TestCase in range(1,T+1):
    data = list(map(int,input().split()))
    ave = sum(data) / len(data)
    print(f"#{int(round(ave,0))}")