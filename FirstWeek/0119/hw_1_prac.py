def fn_d(n) :
    hap = (n % 10)
    i=1
    while True :
        hap += n //(10 * i)
        i += 1
        if i == len(str(n)):
            break
            
    hap += n
    return hap

print(fn_d(91))