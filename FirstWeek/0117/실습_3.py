str_list = input('문자열을 입력하세요. : ')
lower_str_list = str_list.lower()
i = 0
first_list = []
second_list = []
third_list = []
while True :
    first_list.append(lower_str_list[i])
    i += 1
    if lower_str_list[i] == ' ' :
        i += 1
        break
while True :
    second_list.append(lower_str_list[i])
    i += 1
    if lower_str_list[i] == ' ' :
        i += 1
        break
while True :
    third_list.append(lower_str_list[i])
    i += 1
    if lower_str_list[i] == lower_str_list[-1] :
        break
if first_list[-1] == second_list[0] :
    if second_list[-1] == third_list[0]:
        print("pass")
    else :
        print("fail")
else :
    print("fail")
    







''' 이렇게 하는 줄 알았음.
import sys

a,b,c = sys.stdin.readline().rstrip().split()

lowA = a.lower()
lowB = b.lower()
lowC = c.lower()

if lowA[-1] == lowB[0] :
    if lowB[-1] == lowC[0] :
        print("pass")
    else :
        print("fail")
else :
    print("fail")
'''