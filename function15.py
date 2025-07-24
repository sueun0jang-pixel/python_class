
# 함수 정의
import string
import random

def genPass():
    str = string.ascii_lowercase + string.digits
    
    password = ''

    for _ in range(6): #_:변수를 사용하지 않겠다는 의미 
        password += random.choice(str)

    return password

print(genPass())
print(genPass())
print(genPass())


# for x in range(3):
#     ch = random.choice('123456789') 
#     print(ch)