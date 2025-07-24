# 변수에 대한 예제

a = 10
b = 20

print(a+b)

# 자료형 확인
print(type(a))
print(type(b))

# 주소 확인
print(id(a)) 
print(id(b)) 

c = input('숫자를 입력하세요')

c_int = int(c)

if c_int < 10:
    print(f'{c_int}는 {a}보다 작습니다.')
else:
    print(f'{c_int}는 {a}보다 큽니다.')
