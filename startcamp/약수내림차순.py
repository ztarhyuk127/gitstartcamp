T = int(input())
for TestCase in range(1,1+T) :
    num = int(input())
    numlist = []
    yaksu = num
    numlist.append(f"#{TestCase}")
    for i in range(0,num) :
        if num % yaksu == 0 :
            numlist.append(yaksu)
        yaksu -= 1    # 6의 약수 리스트 [#1,6,3,2,1]
    for j in range(0,len(numlist)):
        print(numlist[j],end=" ")
    print()

    
