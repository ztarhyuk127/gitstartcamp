blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}

for i in blood_types :
    if i in blood_dict :
        blood_dict[i] += 1
    else :
        blood_dict[i] = 1
print(blood_dict)