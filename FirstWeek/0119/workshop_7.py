def get_strong_word(a,b):
    hapforA, hapforB = 0, 0
    for i in range(len(a)):
        hapforA += ord(a[i])

    for j in range(len(b)):
        hapforB += ord(b[j])
    
    if hapforA > hapforB :
        return a
    elif hapforA < hapforB :
        return b
    else :
        return a, b

