'''
 T = 테스트 케이스
 H = 높이
 W = 너비
'''
T = int(input())
for TestCase in range(1,T+1):
    num = 1
    H,W = map(int,input().split()) #3,5
    while num <= H * W :
        print(num, end = " ")
        num % W == 0 and print()
        num += 1
            
    
