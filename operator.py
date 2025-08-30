# 대입 연산자
x = 10
y = 15

# 조건 연산자
z = x == y
print("x == y :", z)
z = x != y
print("x != y :", z)
z = x > y
print("x > y :", z)
z = x >= y
print("x < y :", z)
z = x < y
print("x < y :", z)
z = x <= y
print("x <= y :", z)

z=x+y
print("x+y",z)
z=x-y
print("x-y",z)
z=x*y
print("x*y",z)
z=x/y
print("x/y",z)

z=x%y
print("x%y",z)
z=x//y
print("x//y",z)

z=x**y
print("x**y",z)

str_x="hello"
str_y="python"

str_z=str_x+str_y
print("str_x+str_y:",str_z)

# unsupported operand type(s) for -: 'str' and 'str'
# str_z = str_x - str_y
# print("str_x + str_y:", str_z)