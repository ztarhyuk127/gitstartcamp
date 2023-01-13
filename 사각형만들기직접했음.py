T = int(input())
for TestCase in range(1, T+1) :
    
    h , w = map(int, input().split())
    num = 1
    print(f"#{TestCase}")
    for i in range(1,h+1) :
        for j in range(1,w+1):
            print( num,end =" ")
            num+=1
            if j ==w :
                print()