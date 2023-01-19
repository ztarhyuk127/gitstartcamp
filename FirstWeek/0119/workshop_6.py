def get_secret_word(a) :
    hap = 0
    for j in range(len(a)) :
        hap += int(ord(a[j]))
    return hap
   
print(get_secret_word('happy'))