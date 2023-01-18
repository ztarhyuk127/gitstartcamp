s_triangle = input().split()
i_triangle = []
# s_triangle = 
for i in range(len(s_triangle)) :
    s_triangle[i] = int(s_triangle[i])
    i_triangle.append(s_triangle[i])

i_triangle = sorted(i_triangle)
[a,b,c]=i_triangle

if a == b == c :
    print("정삼각형")
elif a == b or b == c or a == c :
    print("이등변삼각형")
elif a**2 + b**2 == c**2 :
    print("직각삼각형")
elif a + b <= c :
    print("삼각형 아님")
else :
    print("삼각형")



