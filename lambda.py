
# 람다 함수에 대한 예제

# def hello(user_name):
#     return "Hello, " + user_name

hello = lambda user_name: 'hello, ' + user_name

print(type(hello)) # function 객체

print(hello('Jse'))