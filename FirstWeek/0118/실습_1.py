s =  'apple,rottenBanana,apple,RoTTenorange,Orange'
s = s.lower().split(',')

for i in range(len(s)) :
    if 'rotten' in s[i] :
        s[i] = s[i][6:]
print(s)

        


