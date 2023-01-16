T = int(input())
for TestCase in range(1, T+1):
    f,b,s = input().split()
    intf, intb = int(f), int(b)
    if s == '+' :
        r = intf + intb
    elif s == '-':
        r = intf - intb
    elif s == '*':
        r = intf * intb
    elif s == '/':
        r = intf // intb
    
    print(f"#{TestCase} {r}")