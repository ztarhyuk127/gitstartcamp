TestCase = int(input())

for TestNum in range(1,TestCase + 1) :
    a, b = map(int,input().split())

    if abs(a - b) == 0 :
        winner = 0
    elif abs(a - b) == 1 :
        if a > b :
            winner = 1
        elif a < b :
            winner = 2
    elif abs(a - b) == 2 :
        if a > b :
            winner = 2
        elif a < b :
            winner = 1
    
    if winner == 0 :
        result = "="
    elif winner == 1 :
        result = "A"
    elif winner == 2 :
        result = "B"

    print(f"#{TestNum} {result}")
