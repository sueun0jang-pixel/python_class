
# 위치 기반 가변 인수 함수에 대한 예제 프로그램

# 함수 정의
def print_info(**kwargs):
    print(f'kwargs : {kwargs}')
    print(f'kwargs 자료형 : {type(kwargs)}')

    for key, value in kwargs.items(): #언패킹
        print(f'{key} : {value}')

# 함수 호출
print_info(username='구름',age=4)  # 키워드 기반 인수
print_info(username='구름',age=4 , gender='왈') # 키워드 기반 인수
