
# 함수 정의

def print_all(a,b,c):
    print(f'a = {a},b = {b},c = {c}')

_list = [1, 2, 3]

print_all(*_list) # print_all(1,2,3)와 같은 코드다 / 함수 호출할때 쓴 언패킹


